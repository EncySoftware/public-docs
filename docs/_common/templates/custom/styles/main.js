(function () {
  'use strict';

  var xrefData = null;
  var loading = false;
  var resultsContainer = null;
  var filterTagsContainer = null;

  // Active filters by member type
  var activeFilters = {
    namespace: true,
    type: true,
    method: true,
    property: true,
    field: true,
    event: true
  };

  function loadXrefMap(callback) {
    if (xrefData) {
      callback(xrefData);
      return;
    }
    if (loading) return;
    loading = true;

    var xrefUrl = new URL('xrefmap.yml', getSiteRoot()).href;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', xrefUrl, true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        xrefData = parseXrefYaml(xhr.responseText);
        callback(xrefData);
      } else {
        console.warn('xrefmap.yml failed to load:', xhr.status, xrefUrl);
      }
      loading = false;
    };
    xhr.onerror = function () {
      console.warn('xrefmap.yml request error:', xrefUrl);
      loading = false;
    };
    xhr.send();
  }

  function getSiteRoot() {
    // _rel — path from the page to the site root (native DocFX mechanism)
    var meta = document.querySelector('meta[name="_rel"]');
    var rel = meta && meta.getAttribute('content');
    if (rel) return new URL(rel, window.location.href);

    // Fallback: search runs only on '/api/...', and api/ is a direct child of
    // the DocFX site root, so count the climb up from the 'api/' segment
    var path = window.location.pathname;
    var apiIdx = path.lastIndexOf('/api/');
    if (apiIdx !== -1) {
      var tail = path.substring(apiIdx + 1);        // 'api/Foo.html'
      var ups = (tail.match(/\//g) || []).length;   // levels up to the site root
      var rel2 = '';
      for (var i = 0; i < ups; i++) rel2 += '../';
      return new URL(rel2 || './', window.location.href);
    }
    return new URL('./', window.location.href);
  }

  function safeMemberHref(rawHref, root) {
    try {
      var url = new URL(rawHref, root);
      if (url.protocol === 'http:' || url.protocol === 'https:') return url.href;
    } catch (e) { /* invalid href — skip it */ }
    return null;
  }

  function parseXrefYaml(text) {
    var items = [];
    var lines = text.split('\n');
    var current = null;

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];

      if (line.indexOf('- uid:') === 0) {
        if (current && current.name && current.href) {
          items.push(current);
        }
        current = { uid: line.substring(7).trim() };
      } else if (current) {
        if (line.indexOf('  name:') === 0 && line.indexOf('name.') === -1
            && line.indexOf('nameWithType') === -1) {
          current.name = line.substring(8).trim();
        } else if (line.indexOf('  href:') === 0) {
          current.href = line.substring(8).trim();
        } else if (line.indexOf('  commentId:') === 0) {
          current.commentId = line.substring(13).trim();
        } else if (line.indexOf('  nameWithType:') === 0 && line.indexOf('nameWithType.') === -1) {
          current.nameWithType = line.substring(16).trim();
        }
      }
    }
    if (current && current.name && current.href) {
      items.push(current);
    }

    return items;
  }

  function getMemberType(item) {
    if (!item.commentId) return '';
    var prefix = item.commentId.charAt(0);
    switch (prefix) {
      case 'M': return 'method';
      case 'P': return 'property';
      case 'F': return 'field';
      case 'E': return 'event';
      case 'T': return 'type';
      case 'N': return 'namespace';
      default: return '';
    }
  }

  function getMemberLabel(type) {
    switch (type) {
      case 'method': return 'M';
      case 'property': return 'P';
      case 'field': return 'F';
      case 'event': return 'E';
      case 'type': return 'T';
      case 'namespace': return 'N';
      default: return '?';
    }
  }

  function getLabelColor(type) {
    switch (type) {
      case 'method': return '#795e26';
      case 'property': return '#001080';
      case 'field': return '#0066a1';
      case 'event': return '#8b3a8f';
      case 'type': return '#267f99';
      case 'namespace': return '#365f91';
      default: return '#3f474d';
    }
  }

  function searchMembers(query, data) {
    if (!query || query.length < 2) return [];
    var lower = query.toLowerCase();
    var results = [];
    var maxResults = 30;

    var seen = {};
    for (var i = 0; i < data.length; i++) {
      var item = data[i];
      var type = getMemberType(item);
      if (!type) continue;
      // Skip if the filter for this type is disabled
      if (!activeFilters[type]) continue;
      var searchName = (item.nameWithType || item.name || '').toLowerCase();
      if (searchName.indexOf(lower) !== -1) {
        var key = (item.name || '') + '|' + (item.href || '');
        if (seen[key]) continue;
        seen[key] = true;
        results.push(item);
        if (results.length >= maxResults) break;
      }
    }

    return results;
  }

  function createResultsContainer() {
    if (resultsContainer) return resultsContainer;

    resultsContainer = document.createElement('div');
    resultsContainer.id = 'toc-member-results';
    resultsContainer.style.cssText =
      'display:none;position:fixed;z-index:99999;background:#ffffff;' +
      'border:1px solid #dce5e7;border-top:none;max-height:400px;' +
      'overflow-y:auto;box-sizing:border-box;' +
      'scrollbar-width:thin;scrollbar-color:#c2ced1 transparent;' +
      'box-shadow:0 12px 30px rgba(9,32,35,0.14);';

    document.body.appendChild(resultsContainer);

    var filterInput = document.getElementById('toc_filter_input');
    if (filterInput) {
      var positionDropdown = function () {
        var rect = filterInput.getBoundingClientRect();
        resultsContainer.style.top = rect.bottom + 'px';
        resultsContainer.style.left = rect.left + 'px';
        resultsContainer.style.width = rect.width + 'px';
      };
      positionDropdown();
      window.addEventListener('resize', positionDropdown);
      window.addEventListener('scroll', positionDropdown, true);
    }

    return resultsContainer;
  }

  function renderResults(results) {
    var container = createResultsContainer();
    while (container.firstChild) container.removeChild(container.firstChild);
    if (!results || results.length === 0) {
      container.style.display = 'none';
      return;
    }

    var root = getSiteRoot();

    for (var i = 0; i < results.length; i++) {
      var item = results[i];
      var type = getMemberType(item);
      var displayName = item.nameWithType || item.name || '';
      var href = safeMemberHref(item.href, root);

      var link = document.createElement('a');
      link.className = 'toc-member-result';
      link.style.cssText =
        'display:flex;align-items:center;gap:8px;padding:5px 10px;' +
        'color:#39484e;text-decoration:none;font-size:12px;' +
        'border-bottom:1px solid #eaf0f1;white-space:nowrap;overflow:hidden;' +
        'text-overflow:ellipsis;';
      if (href) link.href = href;

      var label = document.createElement('span');
      label.style.cssText = 'color:' + getLabelColor(type) +
        ';font-weight:bold;font-size:11px;min-width:14px;text-align:center;';
      label.textContent = getMemberLabel(type);

      var name = document.createElement('span');
      name.style.cssText = 'overflow:hidden;text-overflow:ellipsis;';
      name.title = displayName;        // via property — safe
      name.textContent = displayName;  // text node — no escaping needed

      link.appendChild(label);
      link.appendChild(name);
      container.appendChild(link);
    }

    container.style.display = 'block';
  }

  // --- Filter tags panel ---

  function createFilterTags() {
    if (filterTagsContainer) return;

    filterTagsContainer = document.createElement('div');
    filterTagsContainer.id = 'toc-filter-tags';
    filterTagsContainer.style.cssText =
      'display:none;position:fixed;z-index:100000;' +
      'padding:8px 10px;background:#ffffff;' +
      'border:1px solid #dce5e7;border-radius:4px;' +
      'gap:6px;flex-wrap:wrap;justify-content:center;' +
      'box-shadow:0 12px 30px rgba(9,32,35,0.14);';

    var tags = [
      { key: 'namespace', label: 'N', title: 'Namespaces' },
      { key: 'type',      label: 'T', title: 'Types' },
      { key: 'method',    label: 'M', title: 'Methods' },
      { key: 'property',  label: 'P', title: 'Properties' },
      { key: 'field',     label: 'F', title: 'Fields' },
      { key: 'event',     label: 'E', title: 'Events' }
    ];

    for (var i = 0; i < tags.length; i++) {
      var tag = tags[i];
      var btn = document.createElement('button');
      btn.className = 'filter-tag';
      btn.setAttribute('data-filter', tag.key);
      btn.title = tag.title;
      btn.textContent = tag.label;
      btn.style.cssText =
        'border:1px solid ' + getLabelColor(tag.key) + ';' +
        'background:' + getLabelColor(tag.key) + ';' +
        'color:#ffffff;font-size:12px;font-weight:bold;' +
        'padding:4px 10px;cursor:pointer;border-radius:3px;' +
        'min-width:30px;text-align:center;transition:all 0.15s;' +
        'line-height:1;';

      btn.addEventListener('click', (function (key, button) {
        return function () {
          activeFilters[key] = !activeFilters[key];
          updateTagStyle(button, key);
          triggerSearch();
        };
      })(tag.key, btn));

      filterTagsContainer.appendChild(btn);
    }

    document.body.appendChild(filterTagsContainer);
    // Insert the tags panel after sidefilter
    var sidefilter = document.querySelector('.sidefilter');
    if (sidefilter && sidefilter.parentNode) {
      sidefilter.parentNode.insertBefore(filterTagsContainer, sidefilter.nextSibling);
    }
  }

  function updateTagStyle(button, key) {
    var color = getLabelColor(key);
    if (activeFilters[key]) {
      button.style.background = color;
      button.style.color = '#ffffff';
      button.style.borderColor = color;
      button.style.opacity = '1';
    } else {
      button.style.background = 'transparent';
      button.style.color = '#839097';
      button.style.borderColor = '#a3b0b5';
      button.style.opacity = '0.5';
    }
  }

  function toggleFilterTags() {
    if (!filterTagsContainer) return;
    var visible = filterTagsContainer.style.display === 'flex';
    if (visible) {
      filterTagsContainer.style.display = 'none';
    } else {
      // Position next to the search input
      var filterInput = document.getElementById('toc_filter_input');
      if (filterInput) {
        var rect = filterInput.getBoundingClientRect();
        filterTagsContainer.style.top = (rect.bottom + 4) + 'px';
        filterTagsContainer.style.left = rect.left + 'px';
      }
      filterTagsContainer.style.display = 'flex';
    }
  }

  function triggerSearch() {
    var filterInput = document.getElementById('toc_filter_input');
    if (!filterInput) return;
    var query = filterInput.value.trim();
    if (query.length < 2) return;
    loadXrefMap(function (data) {
      var results = searchMembers(query, data);
      renderResults(results);
    });
  }

  // --- Initialization ---

  function init() {
    // Extended search only on API pages
    var path = window.location.pathname;
    if (path.indexOf('/api/') === -1 && path.indexOf('/api.') === -1) return;

    var filterInput = document.getElementById('toc_filter_input');
    if (!filterInput) return;

    // Styles
    var style = document.createElement('style');
    style.textContent =
      '.toc-member-result:hover{background:#ecfbf7 !important;color:#17212b !important;}' +
      '#toc-member-results::-webkit-scrollbar{width:6px;}' +
      '#toc-member-results::-webkit-scrollbar-track{background:transparent;}' +
      '#toc-member-results::-webkit-scrollbar-thumb{background:#c2ced1;border-radius:3px;}' +
      '.filter-tag:hover{opacity:0.8 !important;}';
    document.head.appendChild(style);

    // Create the tags panel
    createFilterTags();

    // Bind the filter button to toggle the tags (on the icon itself only)
    var filterBtn = document.querySelector('span.glyphicon.glyphicon-filter.filter-icon');
    if (filterBtn) {
      // Attach to the span itself
      filterBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleFilterTags();
      });

      // Make it clickable
      filterBtn.style.cursor = 'pointer';
    }

    var debounceTimer = null;

    filterInput.addEventListener('input', function () {
      var query = filterInput.value.trim();

      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () {
        if (query.length < 2) {
          if (resultsContainer) resultsContainer.style.display = 'none';
          return;
        }
        loadXrefMap(function (data) {
          var results = searchMembers(query, data);
          renderResults(results);
        });
      }, 250);
    });

    // Hide on click outside
    document.addEventListener('click', function (e) {
      if (resultsContainer && !resultsContainer.contains(e.target) &&
          e.target !== filterInput &&
          (!filterTagsContainer || !filterTagsContainer.contains(e.target))) {
        resultsContainer.style.display = 'none';
      }
    });

    // Hide the tags on click outside
    document.addEventListener('click', function (e) {
      if (filterTagsContainer &&
          filterTagsContainer.style.display === 'flex' &&
          !filterTagsContainer.contains(e.target) &&
          (!filterBtn || (e.target !== filterBtn && e.target !== filterBtn.parentElement))) {
        filterTagsContainer.style.display = 'none';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* =============================================================
   Track the current page in the left TOC: highlight it and keep
   its branch expanded across navigation. statictoc marks the
   active node but leaves the tree collapsed (no ".in" on the
   ancestors), so expand them here. Re-applies when docfx
   re-renders the TOC (e.g. after loading toc.html over HTTP).
   ============================================================= */
(function () {
  'use strict';
  function markActive() {
    var toc = document.querySelector('.sidetoc');
    if (!toc) return;
    var links = toc.querySelectorAll('a[href]');
    if (!links.length) return;
    var active = null;
    for (var i = 0; i < links.length; i++) {
      var h = links[i].getAttribute('href') || '';
      if (!h || h.charAt(0) === '#') continue;
      try {
        if (new URL(links[i].href).pathname === location.pathname) { active = links[i]; break; }
      } catch (e) { /* ignore */ }
    }
    if (!active) {
      var here = location.pathname.split('/').pop() || 'index.html';
      for (var j = 0; j < links.length; j++) {
        var f = (links[j].getAttribute('href') || '').split('#')[0].split('/').pop();
        if (f && f === here) { active = links[j]; break; }
      }
    }
    if (!active || !active.closest) return;
    var li = active.closest('li');
    var el = li;
    while (el) {
      if (el.tagName === 'LI') el.classList.add('in');
      el = el.parentElement && el.parentElement.closest ? el.parentElement.closest('li') : null;
    }
    if (li) {
      li.classList.add('active', 'in');
      if (li.scrollIntoView) { try { li.scrollIntoView({ block: 'center' }); } catch (e) { li.scrollIntoView(); } }
    }
  }
  function start() {
    markActive();
    setTimeout(markActive, 250);
    setTimeout(markActive, 800);
    var toc = document.querySelector('.sidetoc');
    if (toc && window.MutationObserver) {
      var t = null;
      new MutationObserver(function () { clearTimeout(t); t = setTimeout(markActive, 50); })
        .observe(toc, { childList: true, subtree: true });
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

/* Add a route back from a versioned DocFX page to its documentation portal. */
(function () {
  'use strict';

  function addDocumentationHomeLink() {
    if (document.querySelector('.documentation-home-link')) return;

    var segments = window.location.pathname.split('/');
    var versionIndex = -1;
    for (var i = 0; i < segments.length; i++) {
      if (/^v[1-9][0-9]*$/.test(segments[i])) {
        versionIndex = i;
        break;
      }
    }
    if (versionIndex === -1) return;

    var header = document.querySelector('#autocollapse .navbar-header');
    if (!header) return;

    var labelMeta = document.querySelector('meta[name="documentation-portal-label"]');
    var label = labelMeta && labelMeta.getAttribute('content');
    if (!label) {
      label = (document.documentElement.lang || '').toLowerCase().indexOf('ru') === 0
        ? 'Центр документации'
        : 'Documentation center';
    }

    var homePath = segments.slice(0, versionIndex + 1).join('/') + '/';
    var link = document.createElement('a');
    link.className = 'documentation-home-link';
    link.href = homePath;
    link.title = label;
    link.setAttribute('aria-label', label);

    var arrow = document.createElement('span');
    arrow.className = 'documentation-home-link__arrow';
    arrow.setAttribute('aria-hidden', 'true');
    arrow.textContent = '←';

    var text = document.createElement('span');
    text.className = 'documentation-home-link__label';
    text.textContent = label;

    link.appendChild(arrow);
    link.appendChild(text);

    var brand = header.querySelector('.navbar-brand');
    if (brand && brand.nextSibling) header.insertBefore(link, brand.nextSibling);
    else header.appendChild(link);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addDocumentationHomeLink);
  } else {
    addDocumentationHomeLink();
  }
})();
