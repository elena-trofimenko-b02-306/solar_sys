# coding: utf-8
# license: GPLv3
from solar_vis import *

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        #r = max(r, body.R)
        """if r<=(body.R+obj.R):
            body.Vx=0.5*((body.Vx**2+body.Vy**2)**0.5)*((body.x-obj.x)/r)
            body.Vy=0.5*((body.Vx**2+body.Vy**2)**0.5)*((body.y-obj.y)/r)"""
        body.Fx += -1*(float(gravitational_constant)*obj.m*body.m*((body.x-obj.x)/r))/r**2
        body.Fy += -1*(float(gravitational_constant)*obj.m*body.m*((body.y-obj.y)/r))/r**2








def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
      # FIXME: Вывести формулы для ускорения, скоростей и координат
    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.Vy = body.Vy +(ay * dt)
    body.Vx = body.Vx+(ax * dt)
    body.x = body.x + (body.Vx * dt)
    body.y = body.y + (body.Vy * dt)


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
