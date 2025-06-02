const originalFetch = window.fetch;
window.fetch = function(resource, init) {
  if (typeof resource === 'string' && resource.includes('/api/public_lobbies')) {
    return Promise.reject(new Error('Request blocked by client'));
  }
  return originalFetch(resource, init);
};
