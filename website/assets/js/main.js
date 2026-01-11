/**
 * Headbangers Ball Archive - Main JavaScript
 * Interactive features and utilities
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
        initMobileMenu();
        initNavigation();
        initScrollEffects();
        initAnimations();
    });

    /**
     * Mobile menu toggle
     */
    function initMobileMenu() {
        const menuBtn = document.getElementById('mobile-menu-btn');
        const mainNav = document.getElementById('main-nav');

        if (!menuBtn || !mainNav) return;

        // Create overlay element
        const overlay = document.createElement('div');
        overlay.className = 'nav-overlay';
        document.body.appendChild(overlay);

        function openMenu() {
            menuBtn.classList.add('active');
            mainNav.classList.add('active');
            overlay.classList.add('active');
            menuBtn.setAttribute('aria-expanded', 'true');
            document.body.style.overflow = 'hidden';
        }

        function closeMenu() {
            menuBtn.classList.remove('active');
            mainNav.classList.remove('active');
            overlay.classList.remove('active');
            menuBtn.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }

        function toggleMenu() {
            if (mainNav.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        }

        menuBtn.addEventListener('click', toggleMenu);
        overlay.addEventListener('click', closeMenu);

        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && mainNav.classList.contains('active')) {
                closeMenu();
            }
        });

        // Close when clicking a nav link
        mainNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }

    /**
     * Navigation enhancements
     */
    function initNavigation() {
        // Highlight current page in navigation
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.main-nav a');

        navLinks.forEach(link => {
            const linkPath = new URL(link.href).pathname;
            if (currentPath === linkPath ||
                (linkPath !== '/' && currentPath.startsWith(linkPath))) {
                link.style.color = 'var(--color-accent)';
            }
        });

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    /**
     * Scroll effects for header
     */
    function initScrollEffects() {
        const header = document.querySelector('.site-header');
        if (!header) return;

        let ticking = false;

        window.addEventListener('scroll', function() {
            if (!ticking) {
                window.requestAnimationFrame(function() {
                    const currentScroll = window.pageYOffset;

                    // Add shadow when scrolled
                    if (currentScroll > 10) {
                        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.5)';
                    } else {
                        header.style.boxShadow = 'none';
                    }

                    ticking = false;
                });

                ticking = true;
            }
        });
    }

    /**
     * Fade-in animations for cards
     */
    function initAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(10px)';
                    entry.target.style.transition = 'opacity 0.2s ease, transform 0.2s ease';

                    // Trigger animation
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 50);

                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe cards for animation
        const animatedElements = document.querySelectorAll(
            '.stat-card, .episode-card, .year-card, .host-item, ' +
            '.era-card, .fact-card, .info-card'
        );

        animatedElements.forEach((el, index) => {
            // Stagger the animations slightly
            el.style.transitionDelay = `${index * 0.02}s`;
            observer.observe(el);
        });
    }

    /**
     * Utility: Format date for display
     */
    window.formatDate = function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    /**
     * Utility: Debounce function for performance
     */
    window.debounce = function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    };


    /**
     * Copy to clipboard utility
     */
    window.copyToClipboard = function(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            return navigator.clipboard.writeText(text);
        } else {
            // Fallback for older browsers
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            return Promise.resolve();
        }
    };

    /**
     * Share episode functionality
     */
    window.shareEpisode = function(title, url) {
        if (navigator.share) {
            navigator.share({
                title: title,
                text: `Check out this Headbangers Ball episode: ${title}`,
                url: url
            }).catch(err => {
                console.log('Share cancelled or failed:', err);
            });
        } else {
            // Fallback: Copy link to clipboard
            copyToClipboard(url).then(() => {
                alert('Link copied to clipboard!');
            });
        }
    };

    /**
     * Local storage utilities for user preferences
     */
    const Storage = {
        set: function(key, value) {
            try {
                localStorage.setItem(`hbb_${key}`, JSON.stringify(value));
            } catch (e) {
                console.warn('LocalStorage not available:', e);
            }
        },

        get: function(key) {
            try {
                const item = localStorage.getItem(`hbb_${key}`);
                return item ? JSON.parse(item) : null;
            } catch (e) {
                console.warn('LocalStorage not available:', e);
                return null;
            }
        },

        remove: function(key) {
            try {
                localStorage.removeItem(`hbb_${key}`);
            } catch (e) {
                console.warn('LocalStorage not available:', e);
            }
        }
    };

    window.HBBStorage = Storage;

    /**
     * Analytics helper (placeholder for future implementation)
     */
    window.trackEvent = function(category, action, label) {
        // Placeholder for analytics tracking
        console.log('Event:', category, action, label);

        // When analytics is implemented, add tracking code here
        // Example: gtag('event', action, { 'event_category': category, 'event_label': label });
    };

    /**
     * Print styles helper
     */
    window.printPage = function() {
        window.print();
    };


    /**
     * Era classification helper
     * Returns the era name based on episode date
     */
    window.getEra = function(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;

        // Kevin Seal era: 1987 - early 1988
        if (year === 1987 || (year === 1988 && month <= 4)) {
            return 'seal';
        }
        // Adam Curry era: 1988 - 1990
        if ((year === 1988 && month > 4) || year === 1989 || year === 1990) {
            return 'curry';
        }
        // Riki Rachtman era: 1990 - 1995
        if (year >= 1990 && year <= 1995) {
            return 'rachtman';
        }
        // MTV2 era: 2003 - 2012
        if (year >= 2003 && year <= 2012) {
            return 'mtv2';
        }
        return 'unknown';
    };

    // Log initialization
    console.log('Headbangers Ball Archive initialized');

})();
