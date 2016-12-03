# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-12-02 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iptables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.GenericIPAddressField(default='0.0.0.0')),
                ('i_comment', models.CharField(blank=True, choices=[('\u9e3f\u53d1\u56fd\u9645', '\u9e3f\u53d1\u56fd\u9645'), ('\u6fb3\u95e8\u5a31\u4e50\u57ce', '\u6fb3\u95e8\u5a31\u4e50\u57ce'), ('\u4e00\u7b52\u56fd\u9645', '\u4e00\u7b52\u56fd\u9645'), ('\u56db\u5b63\u57ce', '\u56db\u5b63\u57ce'), ('\u91d1\u516d\u798f', '\u91d1\u516d\u798f'), ('\u4e91\u9876\u81f3\u5c0a', '\u4e91\u9876\u81f3\u5c0a'), ('\u7b90\u82f1\u4f1a', '\u7b90\u82f1\u4f1a'), ('\u65b0\u6fe0\u5929\u5730', '\u65b0\u6fe0\u5929\u5730'), ('\u6cd5\u62c9\u5229\u4fdd\u65f6\u6377', '\u6cd5\u62c9\u5229\u4fdd\u65f6\u6377'), ('\u6c38\u5229', '\u6c38\u5229'), ('\u91d1\u6c99\u57ce', '\u91d1\u6c99\u57ce'), ('\u6fb3\u95e8\u7f8e\u9ad8\u6885', '\u6fb3\u95e8\u7f8e\u9ad8\u6885'), ('\u65b0\u8461\u4eac', '\u65b0\u8461\u4eac'), ('\u8461\u4eac\u56fd\u9645', '\u8461\u4eac\u56fd\u9645'), ('\u5927\u53d1\u9177\u5ba2', '\u5927\u53d1\u9177\u5ba2'), ('\u6fb3\u95e8\u56fd\u9645', '\u6fb3\u95e8\u56fd\u9645'), ('\u76db\u4e16\u56fd\u9645', '\u76db\u4e16\u56fd\u9645'), ('\u6613\u53d1', '\u6613\u53d1'), ('\u83f2\u5f8b\u5bbe', '\u83f2\u5f8b\u5bbe'), ('\u8bda\u4fe1', '\u8bda\u4fe1'), ('\u535a\u72d7\u5a31\u4e50\u57ce', '\u535a\u72d7\u5a31\u4e50\u57ce'), ('\u5b88\u4fe1\u5a31\u4e50\u57ce', '\u5b88\u4fe1\u5a31\u4e50\u57ce'), ('\u6fb3\u95e8\u5a01\u5c3c\u65af\u4eba', '\u6fb3\u95e8\u5a01\u5c3c\u65af\u4eba'), ('\u91d1\u5b9d\u535a', '\u91d1\u5b9d\u535a')], max_length=50)),
                ('i_table', models.CharField(blank=True, default='filter', max_length=50)),
                ('i_method', models.CharField(default='-I', max_length=10)),
                ('i_chain', models.CharField(default='INPUT', max_length=20)),
                ('i_position', models.CommaSeparatedIntegerField(blank=True, default=3, max_length=30)),
                ('i_source_ip', models.GenericIPAddressField(default='0.0.0.0', null=True)),
                ('i_destination_ip', models.GenericIPAddressField(default='0.0.0.0', null=True)),
                ('i_protocol', models.CharField(default='tcp', max_length=8)),
                ('i_port_method', models.CharField(blank=True, default='--dports', max_length=30)),
                ('i_ports', models.CommaSeparatedIntegerField(blank=True, default='80,443', max_length=30)),
                ('i_states', models.CharField(blank=True, default='NEW,ESTABLISHED', max_length=50)),
                ('i_target', models.CharField(default='ACCEPT', max_length=8)),
                ('i_date_time', models.DateTimeField(auto_now_add=True)),
                ('i_remark', models.CharField(blank=True, max_length=50, null=True)),
                ('i_tag', models.CharField(blank=True, default='\u65b0\u5e73\u53f0', max_length=50)),
            ],
            options={
                'verbose_name': '\u767d\u540d\u5355\u7ba1\u7406',
                'verbose_name_plural': '\u767d\u540d\u5355\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='oldsite_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.GenericIPAddressField(choices=[('47.90.52.200', '\u540e\u53f0\u6e90\u7ad9\u8f6c\u53d1200'), ('47.89.54.223', '\u540e\u53f0\u6e90\u7ad9\u8f6c\u53d1223')], default='47.90.52.200')),
                ('agent', models.CharField(choices=[('\u8bda\u4fe1', '\u8bda\u4fe1'), ('\u6613\u53d1', '\u6613\u53d1'), ('\u83f2\u5f8b\u5bbe', '\u83f2\u5f8b\u5bbe'), ('\u535a\u72d7', '\u535a\u72d7'), ('\u5b88\u4fe1', '\u5b88\u4fe1'), ('\u5a01\u5c3c\u65af\u4eba', '\u5a01\u5c3c\u65af\u4eba'), ('\u7f8e\u9ad8\u6885', '\u7f8e\u9ad8\u6885'), ('\u9177\u5ba2', '\u9177\u5ba2'), ('\u5927\u53d1', '\u5927\u53d1'), ('\u6c38\u5229', '\u6c38\u5229')], default='\u8bda\u4fe1', max_length=50)),
                ('agent_name', models.CharField(choices=[('chengxin', 'chengxin'), ('yifa', 'yifa'), ('flb', 'flb'), ('bogou', 'bogou'), ('shouxin', 'shouxin'), ('amwnsr', 'amwnsr'), ('meigaomei', 'meigaomei'), ('kuke', 'kuke'), ('dafa', 'dafa'), ('yongli', 'yongli')], default='chengxin', max_length=50)),
                ('line', models.CharField(choices=[('203.88.164.73', '203.88.164.73'), ('119.28.13.102', '119.28.13.102'), ('119.9.108.157', '119.9.108.157')], default='203.88.164.73', max_length=50)),
                ('number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('status', models.BooleanField(choices=[(True, '\u4f7f\u7528\u4e2d'), (False, '\u7a7a\u95f2')], default='False')),
                ('comment', models.CharField(blank=True, choices=[('\u7ebf\u8def\u4e00', '\u7ebf\u8def\u4e00'), ('\u7ebf\u8def\u4e8c', '\u7ebf\u8def\u4e8c'), ('\u7ebf\u8def\u4e09', '\u7ebf\u8def\u4e09')], default='\u7ebf\u8def\u4e00', max_length=200)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u540e\u53f0\u7ebf\u8def\u7ba1\u7406',
                'verbose_name_plural': '\u540e\u53f0\u7ebf\u8def\u7ba1\u7406',
            },
        ),
    ]