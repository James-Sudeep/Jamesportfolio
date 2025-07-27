import React, { useState } from 'react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { useToast } from '../hooks/use-toast';
import { useContactForm } from '../hooks/usePortfolioData';

const ContactSection = ({ data }) => {
  const { toast } = useToast();
  const { submitContact, submitting, submitError, submitSuccess, resetForm } = useContactForm();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    company: '',
    message: '',
    inquiry_type: 'general'
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Basic validation
    if (!formData.name || !formData.email || !formData.message) {
      toast({
        title: "Missing Information",
        description: "Please fill in all required fields.",
        variant: "destructive"
      });
      return;
    }

    try {
      const response = await submitContact(formData);
      
      toast({
        title: "Message Sent Successfully! 🎉",
        description: `Your message has been sent. Reference ID: ${response.reference_id}`,
      });

      // Reset form
      setFormData({
        name: '',
        email: '',
        company: '',
        message: '',
        inquiry_type: 'general'
      });
      
    } catch (error) {
      toast({
        title: "Failed to Send Message",
        description: submitError || "Please try again later.",
        variant: "destructive"
      });
    }
  };

  const handleEmailClick = () => {
    window.location.href = `mailto:${data.personal.contact.email}`;
    toast({
      title: "Email Client Opening",
      description: "Your default email client should open now.",
    });
  };

  const handlePhoneClick = () => {
    window.location.href = `tel:${data.personal.contact.phone}`;
    toast({
      title: "Calling...",
      description: "Initiating phone call.",
    });
  };

  const copyToClipboard = (text, label) => {
    navigator.clipboard.writeText(text).then(() => {
      toast({
        title: "Copied! 📋",
        description: `${label} copied to clipboard.`,
      });
    });
  };

  return (
    <section className="contact-section">
      <div className="container">
        <div className="section-header">
          <div className="section-badge">🚀 LET'S CONNECT</div>
          <h2 className="section-title">Ready to Transform Your Infrastructure?</h2>
          <p className="section-description">
            Let's discuss how my expertise can drive your next enterprise transformation initiative.
          </p>
        </div>
        
        <div className="contact-grid">
          <Card className="contact-card">
            <h3 className="contact-card-title">Ready for Your Next Challenge?</h3>
            <p className="contact-card-description">
              I'm currently exploring opportunities with forward-thinking organizations looking to revolutionize 
              their IT infrastructure. Whether you need SCCM expertise, systems architecture, or digital 
              transformation leadership, let's create something extraordinary together.
            </p>
            
            {/* Contact Form */}
            <form onSubmit={handleSubmit} className="contact-form">
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="name">Name *</label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleInputChange}
                    required
                    className="form-input"
                    placeholder="Your full name"
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="email">Email *</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleInputChange}
                    required
                    className="form-input"
                    placeholder="your@email.com"
                  />
                </div>
              </div>
              
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="company">Company</label>
                  <input
                    type="text"
                    id="company"
                    name="company"
                    value={formData.company}
                    onChange={handleInputChange}
                    className="form-input"
                    placeholder="Your company name"
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="inquiry_type">Inquiry Type</label>
                  <select
                    id="inquiry_type"
                    name="inquiry_type"
                    value={formData.inquiry_type}
                    onChange={handleInputChange}
                    className="form-select"
                  >
                    <option value="general">General Inquiry</option>
                    <option value="consulting">SCCM Consulting</option>
                    <option value="employment">Employment Opportunity</option>
                    <option value="collaboration">Collaboration</option>
                  </select>
                </div>
              </div>
              
              <div className="form-group">
                <label htmlFor="message">Message *</label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleInputChange}
                  required
                  className="form-textarea"
                  rows="5"
                  placeholder="Tell me about your project or opportunity..."
                />
              </div>
              
              <Button 
                type="submit"
                className="btn-primary form-submit"
                disabled={submitting}
              >
                {submitting ? 'Sending...' : 'Send Message'}
                <span className="btn-icon">📧</span>
              </Button>
              
              {submitSuccess && (
                <div className="form-success">
                  <p>✅ {submitSuccess.message}</p>
                  <p className="reference-id">Reference: {submitSuccess.reference_id}</p>
                </div>
              )}
            </form>
            
            <div className="contact-divider">or reach out directly</div>
            
            <div className="contact-cta">
              <Button 
                className="btn-primary"
                onClick={handleEmailClick}
              >
                Email Me
                <span className="btn-icon">📧</span>
              </Button>
              <Button 
                variant="outline"
                className="btn-secondary"
                onClick={handlePhoneClick}
              >
                Call Now
                <span className="btn-icon">📱</span>
              </Button>
            </div>
            
            <div className="contact-highlights">
              <h4 className="contact-highlights-title">💡 What I Bring to Your Team</h4>
              <ul className="contact-highlights-list">
                <li>→ 10+ years of enterprise SCCM mastery</li>
                <li>→ Proven track record of $1.5M+ cost savings</li>
                <li>→ Leadership in global transformation projects</li>
                <li>→ 99% customer satisfaction and system uptime</li>
              </ul>
            </div>
          </Card>
          
          <div className="contact-info">
            <div className="contact-item" onClick={() => copyToClipboard(data.personal.contact.email, 'Email')}>
              <div className="contact-icon">📧</div>
              <div className="contact-details">
                <div className="contact-label">Email</div>
                <div className="contact-value">{data.personal.contact.email}</div>
              </div>
            </div>
            
            <div className="contact-item" onClick={() => copyToClipboard(data.personal.contact.phone, 'Phone')}>
              <div className="contact-icon">📱</div>
              <div className="contact-details">
                <div className="contact-label">Phone</div>
                <div className="contact-value">{data.personal.contact.phone}</div>
              </div>
            </div>
            
            <div className="contact-item">
              <div className="contact-icon">🌍</div>
              <div className="contact-details">
                <div className="contact-label">Location</div>
                <div className="contact-value">{data.personal.contact.location}</div>
              </div>
            </div>
            
            <div className="contact-item">
              <div className="contact-icon">🎓</div>
              <div className="contact-details">
                <div className="contact-label">Education</div>
                <div className="contact-value">
                  {data.credentials.education[0].degree} {data.credentials.education[0].field}, {data.credentials.education[0].institution}
                </div>
              </div>
            </div>
            
            <div className="contact-item">
              <div className="contact-icon">🏆</div>
              <div className="contact-details">
                <div className="contact-label">Certifications</div>
                <div className="contact-value">
                  {data.credentials.certifications.map(cert => cert.name).join(', ')}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;