# -*- coding: utf-8 -*-
# © 2016 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Trip Listings 2018',
    'version': '10.0.1.0.0',
    'summary': 'Odoo Course 2018 Lesson 8 Code',
    'author': 'Sunflower IT',
    'website': 'http://sunflowerweb.nl',
    'category': 'Enterprise Specific Management',
    'sequence': 0,
    'depends': [
        'base',
    ],
    'demo': [],
    'data': [
        'data/listing.xml',
        'views/trip_listing.xml',
        'views/trip_listing_category.xml',
        'views/trip_listing_image.xml',
        'views/trip_listing_cities.xml'
    ],
    'application': True,
    'installable': True
}
