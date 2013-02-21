// Copyright 2009 Google Inc. All Rights Reserved.

/**
 * @fileoverview Runs at the end of export.html.
 * @author jumpei@google.com (Jumpei Takeuchi)
 */

var pre = document.getElementById('code');
if (window.location.search.match(/[?&]code=([^&]+)/)) {
  pre.innerHTML = (decodeURIComponent(RegExp.$1)
                   .replace(/&/g, '&amp;')
                   .replace(/</g, '&lt;')
                   .replace(/>/g, '&gt;'));
}

pre.addEventListener('click', function() {
  var selection = window.getSelection();
  selection.removeAllRanges();
  var range = document.createRange();
  range.selectNodeContents(pre);
  selection.addRange(range);
}, false);
