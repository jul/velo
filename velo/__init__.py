# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging

import pkg_resources

from pyramid.config import Configurator

log = logging.getLogger(__name__)


def main(global_config, **settings):
    log.info('Starting...')
    config = Configurator(settings=settings)
    config.include('velo')
    log.info('Ready to serve...')
    return config.make_wsgi_app()


def includeme(config):
    version = pkg_resources.get_distribution('velo').version

    config.include('pyramid_rest')
    config.include('velo.model')

    config.add_static_view('/static/%s' % version, 'velo:static')
    config.add_static_view('/static/{version:\d+\.\d+\.\d+}', 'velo:static')

    config.add_resource('medium', plural_name='media')
    config.add_singular_resource('medium.content')

    config.scan('velo.views')
