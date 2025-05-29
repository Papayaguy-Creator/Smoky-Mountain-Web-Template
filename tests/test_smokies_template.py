import os
import re
import unittest
from datetime import datetime

class SmokiesTemplateTest(unittest.TestCase):
    """Test suite for the Smoky Mountains booking website template."""
    
    def setUp(self):
        """Set up the test environment."""
        self.template_path = '/app/smokies-booking-template.html'
        with open(self.template_path, 'r') as file:
            self.html_content = file.read()
    
    def test_file_exists(self):
        """Test that the HTML file exists."""
        self.assertTrue(os.path.exists(self.template_path))
    
    def test_html_structure(self):
        """Test that the HTML file has proper structure."""
        self.assertIn('<!DOCTYPE html>', self.html_content)
        self.assertIn('<html', self.html_content)
        self.assertIn('<head>', self.html_content)
        self.assertIn('<body', self.html_content)
    
    def test_external_resources(self):
        """Test that external resources are loaded."""
        # Check for Tailwind CSS
        self.assertIn('tailwindcss', self.html_content)
        # Check for Font Awesome
        self.assertIn('font-awesome', self.html_content)
    
    def test_navigation_links(self):
        """Test that navigation links are present."""
        self.assertIn('href="#services"', self.html_content)
        self.assertIn('href="#booking"', self.html_content)
        self.assertIn('href="#prayer"', self.html_content)
        self.assertIn('href="#contact"', self.html_content)
    
    def test_smooth_scrolling(self):
        """Test that smooth scrolling JavaScript is implemented."""
        self.assertIn('scrollIntoView', self.html_content)
        self.assertIn("behavior: 'smooth'", self.html_content)
    
    def test_booking_form(self):
        """Test that booking form exists with required fields."""
        self.assertIn('id="booking-form"', self.html_content)
        self.assertIn('id="name"', self.html_content)
        self.assertIn('id="email"', self.html_content)
        self.assertIn('id="date"', self.html_content)
        self.assertIn('id="service"', self.html_content)
        self.assertIn('required', self.html_content)
    
    def test_date_picker_min_date(self):
        """Test that date picker has minimum date set to today."""
        self.assertIn("document.getElementById('date').min = new Date().toISOString().split('T')[0]", self.html_content)
    
    def test_form_submission(self):
        """Test that form submission creates mailto link."""
        self.assertIn('mailto:', self.html_content)
        self.assertIn('handleBookingSubmit', self.html_content)
        self.assertIn('handlePrayerSubmit', self.html_content)
    
    def test_prayer_form(self):
        """Test that prayer form exists with optional fields."""
        self.assertIn('id="prayer-form"', self.html_content)
        self.assertIn('id="prayer-name"', self.html_content)
        self.assertIn('id="prayer-email"', self.html_content)
        self.assertIn('id="prayer"', self.html_content)
        self.assertIn('id="prayer-updates"', self.html_content)
    
    def test_chatbot_widget(self):
        """Test that chatbot widget exists with toggle functionality."""
        self.assertIn('class="chatbot-toggle"', self.html_content)
        self.assertIn('id="chatbot-widget"', self.html_content)
        self.assertIn('toggleChatbot()', self.html_content)
        self.assertIn('sendMessage()', self.html_content)
    
    def test_chatbot_responses(self):
        """Test that chatbot has rule-based responses."""
        self.assertIn('getRuleBasedResponse', self.html_content)
        self.assertIn('lowerMessage.includes', self.html_content)
        # Check for common question responses
        self.assertIn('services', self.html_content.lower())
        self.assertIn('booking', self.html_content.lower())
        self.assertIn('prayer', self.html_content.lower())
        self.assertIn('price', self.html_content.lower())
    
    def test_responsive_design(self):
        """Test that responsive design is implemented."""
        self.assertIn('@media (max-width:', self.html_content)
        self.assertIn('md:', self.html_content)  # Tailwind responsive prefix
    
    def test_animations(self):
        """Test that animations are implemented."""
        self.assertIn('fade-in', self.html_content)
        self.assertIn('@keyframes', self.html_content)
        self.assertIn('animation:', self.html_content)
    
    def test_placeholder_content(self):
        """Test for placeholder content that needs to be replaced."""
        placeholders = re.findall(r'\[([^\]]+)\]', self.html_content)
        self.assertTrue(len(placeholders) > 0)
        print(f"Found {len(placeholders)} placeholders that need to be replaced:")
        for placeholder in set(placeholders):
            print(f"- {placeholder}")

if __name__ == '__main__':
    unittest.main()
