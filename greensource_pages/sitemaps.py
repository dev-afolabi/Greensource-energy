from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return[
            'index',
            'about',
            'services',
            'solar_design',
            'electrical_design',
            'energy_management',
            'project_management',
            'hvac',
            'maintenance_service',
            'projects',
            'project_details',
            'our_team',
            'testimonial',
            'pricing',
            'gallery',
            'faq',
            'privacy',
            'terms_of_use',
        ]

    def location(self, item):
        return reverse(item)