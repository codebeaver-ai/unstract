const setupProxy = require('./setupProxy');
jest.mock('http-proxy-middleware', () => ({
  createProxyMiddleware: jest.fn(() => 'mock middleware')
}));

describe('setupProxy', () => {
  /**
   * This test verifies that the setupProxy function correctly sets up
   * a proxy middleware for the '/api/v1' path, using the backend URL
   * from the environment variable and enabling changeOrigin.
   */
  test('should set up proxy middleware with correct configuration', () => {
    // Mock the app object
    const mockApp = {
      use: jest.fn()
    };

    // Set the environment variable
    process.env.REACT_APP_BACKEND_URL = 'http://mock-backend-url.com';

    // Call the setupProxy function
    setupProxy(mockApp);

    // Check if app.use was called with the correct arguments
    expect(mockApp.use).toHaveBeenCalledWith(
      '/api/v1',
      'mock middleware'
    );

    // Import the mocked createProxyMiddleware function
    const { createProxyMiddleware } = require('http-proxy-middleware');

    // Check if createProxyMiddleware was called with the correct configuration
    expect(createProxyMiddleware).toHaveBeenCalledWith({
      target: 'http://mock-backend-url.com',
      changeOrigin: true
    });
  });
});