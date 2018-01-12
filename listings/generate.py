#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.cfg')

for i in range(1, 4):
    with open('node'+str(i)+'.cfg', 'w') as f:
        f.write(template.render({
            'ip': '10.20.30.4' + str(i),
            'host': 'node' + str(i)
        }))
