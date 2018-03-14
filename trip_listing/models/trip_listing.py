# -*- coding: utf-8 -*-
#
from openerp import SUPERUSER_ID
import time
from datetime import datetime
from openerp import models, fields, api, _
from bs4 import BeautifulSoup
from datetime import date
from openerp.exceptions import UserError
from openerp import http
from openerp.http import Controller, route, request, Response
import werkzeug.utils
import werkzeug.wrappers
import datetime
import re
import json
import requests
import cgi
import random
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

TRIP_LISTING_TYPES = [
    ("draft", "Draft"),
    ("confirm", "Confirmed"),
    ("active", "Active"),
    ("done", "Done"),
    ("cancel", "Canceled")
]
class TripListing(models.Model):
    _name = 'trip.listing'
    _description = 'Trip Listing'
    _order = 'id desc'

    name = fields.Char('Name')
    title = fields.Char('Listing Name')
    category_id = fields.Many2one('trip.listing.category', 'Category')
    feature_image = fields.Binary('Featured Image')
    partner_id = fields.Many2one('res.partner', 'Created By')
    state = fields.Selection(TRIP_LISTING_TYPES, default='draft', string='states')
    date_start = fields.Datetime('Start Date')
    date_end = fields.Datetime('End Date')
    venue = fields.Char('Venue')
    phone = fields.Char('phone')
    email = fields.Char('email')
    website = fields.Char('website')
    city_id = fields.Many2one('trip.listing.city', 'City')
    location = fields.Char('Location')
    description = fields.Html('Description')
    image_ids = fields.One2many('trip.listing.image', 'listing_id', 'Listing Images')
    attendees = fields.Integer('Attendees')

    #related
    partner_name = fields.Char(related='partner_id.name')
    partner_phone = fields.Char(related='partner_id.phone')
    partner_mobile = fields.Char(related='partner_id.mobile')
    partner_email = fields.Char(related='partner_id.email')
    listing_category = fields.Char(related='category_id.name')

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'trip.listing') or '/'
        ret = super(TripListing, self).create(vals)

        # create images
        if 'image_datas' in vals:
            for image_data in vals['image_datas']:
                image_info = image_data.split(",")
                image = image_info[1]
                vals = {
                    'listing_id': ret.id,
                    'name': ret.title,
                    'image': image
                }
                self.env['trip.listing.image'].create(vals)

        return ret

    @api.multi
    def confirm_listing(self):
        for l in self:
            l.state = 'confirm'

    @api.multi
    def cancel_listing(self):
        for l in self:
            l.state = 'cancel'

    @api.multi
    def activate_listing(self):
        for l in self:
            l.state = 'active'

    @api.multi
    def done_listing(self):
        for l in self:
            l.state = 'done'


class TripListingCategory(models.Model):
    _name = 'trip.listing.category'
    _description = 'Trip Listing Category'
    _order = 'id asc'

    name = fields.Char('Name')
    icon = fields.Char('Icon Name')
    category_image = fields.Binary('Category Image')

class TripListingCity(models.Model):
    _name = 'trip.listing.city'
    _description = 'Trip Listing City'
    _order = 'id asc'

    name = fields.Char('Name')

class TripListingImages(models.Model):
    _name = 'trip.listing.image'
    _description = 'Trip Listing Image'
    _order = 'id asc'

    listing_id = fields.Many2one('trip.listing', 'Listing Name')
    name = fields.Char('Name')
    image = fields.Binary('Icon Name')

