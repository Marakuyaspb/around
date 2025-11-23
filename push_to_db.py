#!/usr/bin/env python
import os
import sqlite3
from django.conf import settings

# make sure Django knows where settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around.settings')
import django
django.setup()

db_path = settings.DATABASES['default']['NAME']
conn = sqlite3.connect(db_path)
cur = conn.cursor()

SQL = """
INSERT OR IGNORE INTO blog_country (country_id, country, slug) VALUES
  (1, 'Бразилия', 'braziliya'),
  (2, 'Канада',   'kanada');

INSERT OR IGNORE INTO blog_region (region_id, country_id, region, slug) VALUES
  (1, 1, 'Рио-де-Жанейро', 'rio-de-zhaneiro'),
  (2, 1, 'Сан-Паулу',      'san-paulu'),
  (3, 1, 'Баия',           'baiya'),
  (4, 2, 'Онтарио',        'ontario'),
  (5, 2, 'Квебек',         'kvebek');

INSERT OR IGNORE INTO blog_place_name (place_name_id, region_id, place_name, place_name_source) VALUES
  (1, 1, 'Рио-де-Жанейро', 'Rio de Janeiro'),
  (2, 2, 'Сан-Паулу',     'São Paulo'),
  (3, 3, 'Салвадор',      'Salvador'),
  (4, 4, 'Торонто',       'Toronto'),
  (5, 5, 'Монреаль',      'Montréal');

INSERT OR IGNORE INTO blog_category (category_id, category, slug) VALUES
  (1, 'Город',   'gorod'),
  (2, 'Природа', 'priroda'),
  (3, 'История', 'istoriya');

INSERT OR IGNORE INTO blog_tag (id, tag) VALUES
  (1, 'путешествие'),
  (2, 'культура'),
  (3, 'пляж'),
  (4, 'горы'),
  (5, 'фестиваль');

INSERT OR IGNORE INTO blog_article
  (article_id, category_id, place_name_id, title, slug,
   text, text_html, img_prev, created_at, updated_at)
VALUES
  (1, 1, 1, 'Рио-де-Жанейро – город контрастов', 'rio-kontrasty',
   'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
   '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>',
   'imgs/1.png', datetime('now'), datetime('now')),

  (2, 2, 2, 'Природа вокруг Сан-Паулу', 'priroda-san-paulu',
   'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
   '<p>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>',
   'imgs/2.png', datetime('now'), datetime('now')),

  (3, 3, 3, 'Исторический Салвадор', 'istoriya-salvador',
   'Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
   '<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>',
   'imgs/3.png', datetime('now'), datetime('now')),

  (4, 1, 4, 'Торонто – мегаполис Канады', 'toronto-megapolis',
   'Duis aute irure dolor in reprehenderit in voluptate velit esse.',
   '<p>Duis aute irure dolor in reprehenderit in voluptate velit esse.</p>',
   'imgs/1.png', datetime('now'), datetime('now')),

  (5, 2, 5, 'Природа Квебека', 'priroda-kvebek',
   'Excepteur sint occaecat cupidatat non proident, sunt in culpa.',
   '<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa.</p>',
   'imgs/2.png', datetime('now'), datetime('now'));

INSERT OR IGNORE INTO blog_article_tags (article_id, tag_id) VALUES
  (1,1), (1,2), (1,3),
  (2,1), (2,4),
  (3,2), (3,5),
  (4,1), (4,2),
  (5,1), (5,4);
"""

cur.executescript(SQL)
conn.commit()
conn.close()
print('✔ Dev-data inserted into SQLite')