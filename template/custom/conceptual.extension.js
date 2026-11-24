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
      if (level === 2 && /^\s*application\s+area\s*[:.]?\s*$/i.test(heading)) return section;
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

// Documentation editor layout v1
(function () {
  var previous = exports.postTransform;
  exports.postTransform = function (model) {
    var layouts = model._textLayout;
    // Apply text metadata here, where identical blocks have occurrence numbers.
    model._textLayout = null;
    model = previous(model);
    model._textLayout = layouts;
    var html = model.conceptual || '', nodes = [], stack = [], match;
    var tokens = /<!--[\s\S]*?-->|<\/?([a-z][a-z0-9]*)\b(?:[^>"']|"[^"]*"|'[^']*')*>/gi;
    while ((match = tokens.exec(html))) {
      if (!match[1]) continue;
      var name = match[1].toLowerCase(), tag = match[0];
      if (tag.charAt(1) === '/') {
        for (var i = stack.length - 1; i >= 0; i--) if (stack[i].name === name) {
          var node = stack[i]; node.body = html.slice(node.openEnd, match.index); node.end = tokens.lastIndex;
          stack.length = i; break;
        }
      } else {
        var node = {name:name, start:match.index, openEnd:tokens.lastIndex, end:tokens.lastIndex, tag:tag, body:'', parent:stack[stack.length-1]};
        nodes.push(node);
        if (!/^(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)$/.test(name) && !/\/>$/.test(tag)) stack.push(node);
      }
    }
    function decode(text) {
      return text.replace(/&#x([0-9a-f]+);/gi,function(_,n){return String.fromCharCode(parseInt(n,16));})
        .replace(/&#([0-9]+);/g,function(_,n){return String.fromCharCode(parseInt(n,10));})
        .replace(/&(amp|lt|gt|quot|apos|nbsp);/g,function(_,n){return {amp:'&',lt:'<',gt:'>',quot:'"',apos:"'",nbsp:' '}[n];});
    }
    function textOf(body) { return decode(body.replace(/<[^>]*>/g,' ')).replace(/\s+/g,' ').trim(); }
    function attr(node, name) { var m = new RegExp('\\b'+name+'=["\x27]([^"\x27]*)["\x27]').exec(node.tag); return m ? decode(m[1]) : ''; }
    function css(node, value) {
      if (/\bstyle="/.test(node.tag)) node.tag = node.tag.replace(/style="([^"]*)"/,function(_,s){return 'style="'+s+';'+value+'"';});
      else node.tag = node.tag.replace(/(\/?>)$/,' style="'+value+'"$1');
    }
    function addClass(node, value) {
      if (/\bclass="/.test(node.tag)) node.tag = node.tag.replace(/class="([^"]*)"/,function(_,s){return 'class="'+s+' '+value+'"';});
      else node.tag = node.tag.replace(/(\/?>)$/,' class="'+value+'"$1');
    }
    var occurrences = {}, insertions = [];
    nodes.forEach(function(node) {
      if (!/^(p|h[1-6]|li|td|th|summary)$/.test(node.name)) return;
      var text = textOf(node.body), key = node.name+'\x00'+text, occurrence = occurrences[key] || 0;
      occurrences[key] = occurrence + 1;
      (layouts || []).forEach(function(layout) {
        if ((layout.tag || 'p') !== node.name || layout.text !== text || (layout.occurrence != null && layout.occurrence !== occurrence)) return;
        if (typeof layout.leftPx !== 'number' || typeof layout.topPx !== 'number') return;
        addClass(node,'guide-text-saved');
        css(node,'--guide-text-left:'+layout.leftPx+'px;--guide-text-top:'+layout.topPx+'px;margin-inline-start:'+layout.leftPx+'px;padding-top:'+layout.topPx+'px;');
      });
    });
    var figures = nodes.filter(function(node){return node.name==='p' && /<img\b/.test(node.body) && !textOf(node.body);});
    var rows = model._editorImageRows || {};
    (rows.separate || []).forEach(function(index){
      var node=figures[index]; if (!node) return;
      addClass(node,'guide-image-separate');
      insertions.push({start:node.start,end:node.start,value:'<span class="guide-image-break" hidden></span>'});
    });
    (rows.groups || []).forEach(function(row){
      var members=figures.slice(row.first,row.first+row.count);
      if (members.length!==row.count || row.count<1) return;
      for(var i=1;i<members.length;i++) if (html.slice(members[i-1].end,members[i].start).trim()) return;
      members.forEach(function(node){css(node,'display:block;flex:0 1 auto;min-width:0;margin:0;padding:0;');});
      insertions.push({start:members[0].start,end:members[0].start,value:'<div class="guide-editor-image-row" style="display:flex;gap:'+row.gapPx+'px;margin-inline-start:'+(row.marginPx||0)+'px;padding-left:'+row.leftPx+'px;padding-top:'+row.topPx+'px;">'});
      var end=members[members.length-1].end;
      insertions.push({start:end,end:end,value:'</div>'});
    });
    var imageOccurrences={};
    function imageKey(src) { return src.replace(/^~\//,'').replace(/^.*?assets\//,'assets/'); }
    nodes.filter(function(node){return node.name==='img';}).forEach(function(node){
      var src=imageKey(attr(node,'src')), occurrence=imageOccurrences[src]||0; imageOccurrences[src]=occurrence+1;
      (model._editorInlineImages || []).forEach(function(layout){
        if (imageKey(layout.src)!==src || layout.occurrence!==occurrence) return;
        if (layout.widthPx!=null) {
          css(node,'width:'+layout.widthPx+'px;height:auto;max-width:100%;');
          node.tag=node.tag.replace(/\sdata-guide-width="[^"]*"/g,'').replace(/(\/?>)$/,' data-guide-width="'+layout.widthPx+'"$1');
        }
        if(layout.leftPx!=null || layout.topPx!=null){
          insertions.push({start:node.start,end:node.start,value:'<span class="guide-editor-inline-image" style="display:inline-block;padding-left:'+(layout.leftPx||0)+'px;padding-top:'+(layout.topPx||0)+'px;">'});
          insertions.push({start:node.end,end:node.end,value:'</span>'});
        }
      });
    });
    nodes.forEach(function(node){if(node.tag!==html.slice(node.start,node.openEnd))insertions.push({start:node.start,end:node.openEnd,value:node.tag});});
    insertions.sort(function(a,b){return b.start-a.start || b.end-a.end;});
    insertions.forEach(function(edit){html=html.slice(0,edit.start)+edit.value+html.slice(edit.end);});
    model.conceptual=html;return model;
  };
})();
