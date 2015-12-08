# -*- coding: utf-8 -*-
import pytest
from django.contrib import admin
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_hearing_admin_renders(admin_client):
    url = reverse('admin:democracy_hearing_add')
    response = admin_client.get(url)
