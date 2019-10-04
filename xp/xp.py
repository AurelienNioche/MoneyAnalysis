import numpy as np

from analysis.tools.conversion import Converter

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from game.models import User, Room, Choice

from backup import backup, structure

DATA_FOLDER = f"data"
DATA_FILE = f"{DATA_FOLDER}/xp_data.p"


def _load_data_from_db():

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
        success = np.zeros((n, t_max), dtype=bool)
        prod = np.zeros(n, dtype=int)
        cons = np.zeros(n, dtype=int)

        for i, u in enumerate(users):

            cons[i] = Converter.convert_value(u.consumption_good,
                                              n_good=n_good)
            prod[i] = Converter.convert_value(u.production_good,
                                              n_good=n_good)

            gender[i] = u.gender == 'male'
            age[i] = u.age

            r = Room.objects.get(id=u.room_id)
            n_good = r.n_type

            # Preprocess the data
            for t in range(t_max):

                c = Choice.objects.get(room_id=r.id, t=t, user_id=u.id)

                in_hand[i, t] = Converter.convert_value(c.good_in_hand,
                                                        n_good=n_good)
                desired[i, t] = Converter.convert_value(c.desired_good,
                                                        n_good=n_good)
                success[i, t] = c.success

        data_session[idx] = \
            structure.DataXPSession(
                age=age, in_hand=in_hand, desired=desired,
                prod=prod, cons=cons,
                n_good=n_good, t_max=t_max,
                gender=gender, success=success)
        room_n_good[idx] = n_good
        room_uniform[idx] = len(np.unique([int(i)
                                           for i in r.types.split("/")])) == 1

    return data_session, room_n_good, room_uniform


def get_data(force=False, verbose=True):

    if force or not os.path.exists(DATA_FILE):

        data = _load_data_from_db()
        backup.save(obj=data, file_name=DATA_FILE, verbose=verbose)

    else:

        data = backup.load(DATA_FILE, verbose=verbose)

    return data
