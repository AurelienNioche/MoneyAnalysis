# MoneyAnalysis
# Copyright (C) 2018  Aurélien Nioche, Basile Garcia & Nicolas Rougier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np

from format.conversion import Converter

# Django specific settings
import os

# from analysis.experiment.evolution import evolution_direct
# from analysis.experiment.graph import fig_evo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from game.models import User, Room, Choice

from backup import backup, structure

# SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
# ROOT_FOLDER = f"{SCRIPT_FOLDER}/../../"

DATA_FOLDER = f"data"
# FIG_FOLDER = f"{ROOT_FOLDER}/fig"

DATA_FILE = f"{DATA_FOLDER}/xp_data.p"


def _load__data_from_db():

    rooms = Room.objects.all().order_by('id')

    n_rooms = len(rooms)

    # list of DataXpSession
    data_session = np.zeros(n_rooms, dtype=object)
    room_n_good = np.zeros(n_rooms, dtype=int)
    room_uniform = np.zeros(n_rooms, dtype=bool)

    for idx, r in enumerate(rooms):

        n_good = r.n_type
        t_max = r.t_max

        users = User.objects.filter(room_id=r.id).order_by('id')
        n = len(users)

        age = np.zeros(n, dtype=int)
        gender = np.zeros(n, dtype=bool)
        in_hand = np.zeros((n, t_max), dtype=int)
        desired = np.zeros((n, t_max), dtype=int)
        prod = np.zeros(n, dtype=int)
        cons = np.zeros(n, dtype=int)

        for i, u in enumerate(users):

            cons[i] = Converter.convert_value(u.consumption_good, n_good=n_good)
            prod[i] = Converter.convert_value(u.production_good, n_good=n_good)

            gender[i] = u.gender == 'male'
            age[i] = u.age

            r = Room.objects.get(id=u.room_id)
            n_good = r.n_type

            # Preprocess the data
            for t in range(t_max):

                c = Choice.objects.get(room_id=r.id, t=t, user_id=u.id)

                in_hand[i, t] = Converter.convert_value(c.good_in_hand, n_good=n_good)
                desired[i, t] = Converter.convert_value(c.desired_good, n_good=n_good)

        data_session[idx] = \
            structure.DataXPSession(
                age=age, in_hand=in_hand, desired=desired, prod=prod, cons=cons,
                n_good=n_good, t_max=t_max, gender=gender)
        room_n_good[idx] = n_good
        room_uniform[idx] = len(np.unique([int(i) for i in r.types.split("/")])) == 1

    return data_session, room_n_good, room_uniform


def get_data(force=False):

    if force or not os.path.exists(DATA_FILE):

        data = _load__data_from_db()
        backup.save(obj=data, file_name=DATA_FILE)

    else:

        data = backup.load(DATA_FILE)

    return data
