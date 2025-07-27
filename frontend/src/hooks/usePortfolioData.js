import { useState, useEffect } from 'react';
import { portfolioService, handleApiResponse, handleApiError } from '../services/portfolioService';

// Custom hook for loading portfolio data
export const usePortfolioData = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadPortfolioData = async () => {
      try {
        setLoading(true);
        setError(null);

        // Load all portfolio data in parallel
        const [
          personalResponse,
          skillsResponse,
          experienceResponse,
          projectsResponse,
          aboutResponse,
          credentialsResponse
        ] = await Promise.all([
          portfolioService.getPersonalInfo(),
          portfolioService.getSkills(),
          portfolioService.getExperience(),
          portfolioService.getProjects(),
          portfolioService.getAbout(),
          portfolioService.getCredentials()
        ]);

        // Extract data from API responses
        const portfolioData = {
          personal: handleApiResponse(personalResponse),
          skills: handleApiResponse(skillsResponse),
          experience: handleApiResponse(experienceResponse),
          projects: handleApiResponse(projectsResponse),
          about: handleApiResponse(aboutResponse),
          credentials: handleApiResponse(credentialsResponse)
        };

        // Add computed stats for easy access
        portfolioData.stats = portfolioData.personal.stats;

        setData(portfolioData);
        
        // Track page visit
        portfolioService.trackVisit({
          page: 'portfolio_loaded',
          user_agent: navigator.userAgent,
          referrer: document.referrer
        });

      } catch (err) {
        const errorMessage = handleApiError(err, 'Failed to load portfolio data');
        setError(errorMessage);
        console.error('Portfolio data loading error:', err);
      } finally {
        setLoading(false);
      }
    };

    loadPortfolioData();
  }, []);

  return { data, loading, error };
};

// Custom hook for contact form
export const useContactForm = () => {
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState(null);
  const [submitSuccess, setSubmitSuccess] = useState(null);

  const submitContact = async (contactData) => {
    try {
      setSubmitting(true);
      setSubmitError(null);
      setSubmitSuccess(null);

      const response = await portfolioService.submitContact(contactData);
      
      if (response.success) {
        setSubmitSuccess({
          message: response.message,
          reference_id: response.reference_id
        });
        return response;
      } else {
        throw new Error(response.error || 'Failed to submit contact form');
      }
    } catch (err) {
      const errorMessage = handleApiError(err, 'Failed to send message');
      setSubmitError(errorMessage);
      throw err;
    } finally {
      setSubmitting(false);
    }
  };

  const resetForm = () => {
    setSubmitError(null);
    setSubmitSuccess(null);
  };

  return {
    submitContact,
    submitting,
    submitError,
    submitSuccess,
    resetForm
  };
};

// Custom hook for analytics tracking
export const useAnalytics = () => {
  const trackPageView = (pageName) => {
    portfolioService.trackVisit({
      page: pageName,
      user_agent: navigator.userAgent,
      referrer: document.referrer
    });
  };

  const trackEvent = (eventName, eventData = {}) => {
    portfolioService.trackVisit({
      page: `event_${eventName}`,
      user_agent: navigator.userAgent,
      referrer: document.referrer,
      ...eventData
    });
  };

  return { trackPageView, trackEvent };
};