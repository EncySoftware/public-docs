// The original article URLs are at the book root. Show their chapter TOC there,
// and keep the shared client-side search active for an empty root prefix.
exports.postTransform = function (model) {
  model._disableToc = false;
  if (!model._rel) model._rel = './';
  return model;
};
