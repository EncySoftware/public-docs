// Figure spacing is shared by the manual; the structured guide layout is opt-in.
exports.postTransform = function (model) {
  var content = (model.rawTitle || '') + (model.conceptual || '');
  function withImageWidth(tag, width) {
    if (typeof width !== 'number' || !isFinite(width) || width < 1 || width > 4000) return tag;
    var sizing = '--guide-image-width:' + width + 'px;';
    if (/\bstyle="/.test(tag)) tag = tag.replace('style="', 'style="' + sizing);
    else tag = tag.replace(/(\/?>)$/, ' style="' + sizing + '"$1');
    return tag.replace(/(\/?>)$/, ' data-guide-width="' + width + '"$1');
  }
  if (model._documentationGuide) content = content.replace(
    /<p(?:\s[^>]*)?>\s*<strong(?:\s[^>]*)?>[^<]+<\/strong>\s*<\/p>/g,
    function (paragraph) {
      return paragraph.replace(/^<p\b([^>]*)>/, function (tag, attributes) {
        if (/\bclass="/.test(attributes)) {
          return tag.replace(/class="([^"]*)"/, 'class="$1 guide-subheading"');
        }
        return '<p' + attributes + ' class="guide-subheading">';
      });
    }
  );
  if (model._textLayout) {
    content = content.replace(/<p\b[^>]*>([\s\S]*?)<\/p>/g, function (paragraph, body) {
      var text = body.replace(/<[^>]*>/g, ' ')
        .replace(/&#x([0-9a-f]+);/gi, function (_, code) { return String.fromCharCode(parseInt(code, 16)); })
        .replace(/&#([0-9]+);/g, function (_, code) { return String.fromCharCode(parseInt(code, 10)); })
        .replace(/&(amp|lt|gt|quot|apos|nbsp);/g, function (_, name) {
          return { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' }[name];
        }).replace(/\s+/g, ' ').trim();
      for (var i = 0; i < model._textLayout.length; i++) {
        var layout = model._textLayout[i];
        if (layout.text !== text || typeof layout.leftPx !== 'number' || typeof layout.topPx !== 'number') continue;
        var spacing = '--guide-text-left:' + layout.leftPx + 'px;--guide-text-top:' + layout.topPx + 'px;';
        return paragraph.replace(/^<p\b[^>]*>/, function (tag) {
          if (/\bclass="/.test(tag)) tag = tag.replace(/class="([^"]*)"/, 'class="$1 guide-text-saved"');
          else tag = tag.slice(0, -1) + ' class="guide-text-saved">';
          if (/\bstyle="/.test(tag)) return tag.replace('style="', 'style="' + spacing);
          return tag.slice(0, -1) + ' style="' + spacing + '">';
        });
      }
      return paragraph;
    });
  }
  // Indent complete illustration blocks without shifting inline UI icons.
  var introductionEnd = -1;
  var figureOccurrences = {};
  content = content.replace(
    /<p(?:\s[^>]*)?>(?:\s|&nbsp;|<\/?(?:a|span|strong|em|b|i|br)\b[^>]*>|<img\b[^>]*>)+<\/p>/g,
    function (paragraph, offset) {
      var firstImage = /<img\b[^>]*\bsrc="([^"]+)"/.exec(paragraph);
      if (!firstImage) return paragraph;
      var isIntroduction = /<\/h1>\s*$/.test(content.slice(0, offset)) ||
        (introductionEnd >= 0 && /^\s*$/.test(content.slice(introductionEnd, offset)));
      if (isIntroduction) introductionEnd = offset + paragraph.length;
      var imageKey = firstImage && firstImage[1].replace(/^.*?assets\//, '');
      var saved = model._figureLayout && model._figureLayout[imageKey];
      var occurrence = figureOccurrences[imageKey] || 0;
      figureOccurrences[imageKey] = occurrence + 1;
      if (Array.isArray(saved)) saved = saved[occurrence];
      var hasSavedLayout = saved && typeof saved.leftPx === 'number' &&
        typeof saved.topPx === 'number' && saved.leftPx >= 0 && saved.leftPx <= 400 &&
        saved.topPx >= 0 && saved.topPx <= 160;
      var figureClasses = 'guide-figure' + (isIntroduction ? ' guide-figure-intro' : '') + (hasSavedLayout ? ' guide-figure-saved' : '');
      paragraph = paragraph.replace(/^<p\b([^>]*)>/, function (tag, attributes) {
        if (/\bclass="/.test(attributes)) {
          return tag.replace(/class="([^"]*)"/, 'class="$1 ' + figureClasses + '"');
        }
        return '<p' + attributes + ' class="' + figureClasses + '">';
      });
      if (hasSavedLayout) {
        var spacing = '--guide-figure-left:' + saved.leftPx + 'px;--guide-figure-top:' + saved.topPx + 'px;';
        paragraph = paragraph.replace(/^<p\b[^>]*>/, function (tag) {
          if (/\bstyle="/.test(tag)) return tag.replace('style="', 'style="' + spacing);
          return tag.slice(0, -1) + ' style="' + spacing + '">';
        });
      }
      if (saved && Array.isArray(saved.imageWidths)) {
        var imageIndex = 0;
        paragraph = paragraph.replace(/<img\b[^>]*>/g, function (tag) {
          return withImageWidth(tag, saved.imageWidths[imageIndex++]);
        });
      }
      return paragraph.replace(/^(<p\b[^>]*>)([\s\S]*)(<\/p>)$/, '$1<span class="guide-figure-content">$2</span>$3');
    }
  );
  // Status icons keep their inline position; standalone screenshots retain their size.
  if (model._inlineImageWidth) content = content.replace(
    /<p\b[^>]*class="[^"]*\bguide-figure\b[^"]*"[^>]*>[\s\S]*?<\/p>|<img\b[^>]*>/g,
    function (tag) { return /^<img\b/.test(tag) ? withImageWidth(tag, model._inlineImageWidth) : tag; }
  );
  // Mark section contents without changing the editor's block structure.
  function markSections(level) {
    var pattern = new RegExp('(<h' + level + '\\b[^>]*>)([\\s\\S]*?)(<\\/h' + level + '>)([\\s\\S]*?)(?=<h[1-' + level + ']\\b|$)', 'gi');
    var className = 'guide-h' + level + '-content';
    content = content.replace(pattern, function (section, opening, title, closing, body) {
      var heading = title.replace(/<[^>]*>/g, '').replace(/&nbsp;|&#160;|&#xA0;/gi, ' ');
      if (level === 2 && /^\s*(?:application\s+area|anwendungsbereich|ambito\s+di\s+applicazione)\s*[:.]?\s*$/i.test(heading)) return section;
      var depth = 0;
      body = body.replace(/<!--[\s\S]*?-->|<\/?([a-z][a-z0-9]*)\b(?:[^>"']|"[^"]*"|'[^']*')*>/gi,
        function (tag, name) {
          if (!name) return tag;
          if (tag.charAt(1) === '/') {
            depth = Math.max(0, depth - 1);
            return tag;
          }
          if (depth === 0 && /^(p|ul|ol|dl|blockquote|pre|table|details|div|section|figure|h[3-6]|hr)$/i.test(name) &&
              (level === 2 || !/^h[3-6]$/i.test(name))) {
            var blockClass = className;
            if (model._releaseNotes && level === 2 && /^h3$/i.test(name)) blockClass += ' release-note-section';
            if (model._releaseNotes && ((level === 2 && /^h[4-6]$/i.test(name)) ||
                (level === 3 && !/\bguide-figure\b/.test(tag)))) {
              blockClass += ' release-note-content';
            }
            if (/\bclass=(["'])/.test(tag)) tag = tag.replace(/class=(["'])(.*?)\1/, function (_, quote, classes) {
              return 'class=' + quote + classes + ' ' + blockClass + quote;
            });
            else tag = tag.replace(/(\/?>)$/, ' class="' + blockClass + '"$1');
          }
          if (!/^(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)$/i.test(name) && !/\/>$/.test(tag)) depth++;
          return tag;
        });
      return opening + title + closing + body;
    });
  }
  markSections(2);
  markSections(3);
  model.rawTitle = '';
  var layoutClass = model._operationReference ? 'operation-reference' : (model._documentationGuide ? 'documentation-guide' : '');
  model.conceptual = layoutClass ? '<div class="' + layoutClass + '">\n' + content + '\n</div>' : content;
  return model;
};
