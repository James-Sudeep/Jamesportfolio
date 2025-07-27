import axios from 'axios';

const API_BASE = process.env.REACT_APP_BACKEND_URL + '/api';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`📡 API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('📡 API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    console.log(`✅ API Response: ${response.config.url} - ${response.status}`);
    return response;
  },
  (error) => {
    console.error('❌ API Response Error:', error);
    
    // Handle different error types
    if (error.response) {
      // Server responded with error status
      const { status, data } = error.response;
      console.error(`Server Error ${status}:`, data);
    } else if (error.request) {
      // Request made but no response received
      console.error('Network Error:', error.request);
    } else {
      // Something else happened
      console.error('Request Setup Error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

export const portfolioService = {
  // Portfolio data endpoints
  async getPersonalInfo() {
    try {
      const response = await apiClient.get('/portfolio/personal');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch personal info: ${error.message}`);
    }
  },

  async getSkills() {
    try {
      const response = await apiClient.get('/portfolio/skills');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch skills: ${error.message}`);
    }
  },

  async getExperience() {
    try {
      const response = await apiClient.get('/portfolio/experience');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch experience: ${error.message}`);
    }
  },

  async getProjects() {
    try {
      const response = await apiClient.get('/portfolio/projects');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch projects: ${error.message}`);
    }
  },

  async getAbout() {
    try {
      const response = await apiClient.get('/portfolio/about');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch about info: ${error.message}`);
    }
  },

  async getCredentials() {
    try {
      const response = await apiClient.get('/portfolio/credentials');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch credentials: ${error.message}`);
    }
  },

  // Contact endpoint
  async submitContact(contactData) {
    try {
      const response = await apiClient.post('/contact/message', contactData);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to submit contact form: ${error.message}`);
    }
  },

  // Analytics endpoint
  async trackVisit(visitData) {
    try {
      const response = await apiClient.post('/analytics/visit', visitData);
      return response.data;
    } catch (error) {
      // Don't throw error for analytics - it's not critical
      console.warn('Failed to track visit:', error.message);
      return null;
    }
  },

  // Health check
  async healthCheck() {
    try {
      const response = await apiClient.get('/health');
      return response.data;
    } catch (error) {
      throw new Error(`Health check failed: ${error.message}`);
    }
  }
};

// Utility function to handle API responses
export const handleApiResponse = (response) => {
  if (response && response.success) {
    return response.data;
  } else {
    throw new Error(response?.error || 'API request failed');
  }
};

// Utility function for error handling in components
export const handleApiError = (error, defaultMessage = 'Something went wrong') => {
  console.error('API Error:', error);
  
  if (error.response?.data?.detail) {
    return error.response.data.detail;
  } else if (error.message) {
    return error.message;
  } else {
    return defaultMessage;
  }
};

export default portfolioService;