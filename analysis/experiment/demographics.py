import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec
import scipy.stats
import statsmodels.stats.multitest

from analysis.graph.tools.violin import violin

from game.models import User, Room, Choice

import string


N_DEMOGRAPHIC_VARIABLES = 2  # Gender and age
GENDER_IDX = 0
AGE_IDX = 1

MALE = 0
FEMALE = 1


def run():

    print("\n********* Demographics ***********\n")
    users = User.objects.all()
    ages = [u.age for u in users]
    print(f'Age = {np.mean(ages):.2f} (+/- {np.std(ages):.2f} STD)')
    sex = [u.gender for u in users]
    print(f'Female = {sex.count("female") / len(sex) * 100:.2f}%')
    print()


def _figure_gender(demographic_data):

    """
    :param male_data: dictionary with measure names as keys
    :param female_data: dictionary with measure names as keys
    :return:
    """
    n_measure = demographic_data.shape[1] - N_DEMOGRAPHIC_VARIABLES

    male_bool = demographic_data[:, GENDER_IDX] == MALE
    female_bool = demographic_data[:, GENDER_IDX] == FEMALE

    fig = plt.figure(figsize=(5, 8), dpi=200)

    gs = matplotlib.gridspec.GridSpec(nrows=n_measure, ncols=1)

    axes = []
    for i in range(n_measure):
        ax = fig.add_subplot(gs[i, 0])
        axes.append(ax)

    color = ("C0", "C9")

    for i in range(n_measure):

        male_data = demographic_data[male_bool, N_DEMOGRAPHIC_VARIABLES + i]
        female_data = demographic_data[female_bool, N_DEMOGRAPHIC_VARIABLES + i]

        violin(ax=axes[i],
               data=[
                   male_data,
                   female_data
               ],
               color=color, edgecolor="white", alpha=0.8)
        axes[i].set_ylabel("Score")
        axes[i].set_ylim((-0.01, 1.01))

    for i in range(n_measure-1):
        axes[i].set_xticks([])
    axes[-1].set_xticklabels(['Male', 'Female'])

    plt.tight_layout()

    ax = fig.add_subplot(gs[:, :], zorder=-10)

    plt.axis("off")

    for i in range(n_measure):
        letter = string.ascii_uppercase[i]
        y = (n_measure-1-i)/n_measure
        ax.text(
            s=letter, x=-0.13, y=y, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes,
            fontsize=20)

    plt.savefig('fig/supplementary_gender.pdf')
    plt.close()


def _figure_age(demographic_data):

    n_measure = demographic_data.shape[1] - N_DEMOGRAPHIC_VARIABLES

    fig = plt.figure(figsize=(5, 8), dpi=200)

    gs = matplotlib.gridspec.GridSpec(nrows=n_measure, ncols=1)

    axes = []
    for i in range(n_measure):
        ax = fig.add_subplot(gs[i, 0])
        axes.append(ax)

    for i in range(n_measure):
        # Do the scatter plot
        axes[i].scatter(
            demographic_data[:, AGE_IDX],
            demographic_data[:, N_DEMOGRAPHIC_VARIABLES+i],
            facecolor="black", edgecolor='white', s=15, alpha=1)

        axes[i].set_ylabel("Score")
        axes[i].set_ylim((-0.01, 1.01))

    for i in range(n_measure-1):
        axes[i].set_xticks([])
    axes[-1].set_xlabel('Age')

    # axes[0].set_ylabel("Score")

    plt.tight_layout()

    ax = fig.add_subplot(gs[:, :], zorder=-10)

    plt.axis("off")

    for i in range(n_measure):
        letter = string.ascii_uppercase[i]
        y = (n_measure - 1 - i) / n_measure
        ax.text(
            s=letter, x=-0.13, y=y, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes,
            fontsize=20)

    plt.savefig('fig/supplementary_age.pdf')
    plt.close()


def _stats_gender(demographic_data):

    n_measure = demographic_data.shape[1] - N_DEMOGRAPHIC_VARIABLES

    male_bool = demographic_data[:, GENDER_IDX] == MALE
    female_bool = demographic_data[:, GENDER_IDX] == FEMALE

    n = demographic_data.shape[0]

    ps = []

    for i in range(n_measure):

        male_data = demographic_data[male_bool, N_DEMOGRAPHIC_VARIABLES + i]
        female_data = demographic_data[female_bool, N_DEMOGRAPHIC_VARIABLES + i]

        for s_data, s_name in zip((male_data, female_data), ('male', 'female')):
            m = np.mean(s_data)
            s = np.std(s_data)
            print(f"Measure {i} for {s_name}: mean={m:.02f} std={s:.02f}")

        u, p = scipy.stats.mannwhitneyu(male_data, female_data)
        print(f'Mann-Whitney rank test for sex - measure {i}: u={u}, p={p:.3f}, n={n}')
        print()
        ps.append(p)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01, method="b")

    print(f"p_corrected = ", [f"{i:.3f}" for i in p_corr])
    print()


def _stats_age(demographic_data):

    n_measure = demographic_data.shape[1] - N_DEMOGRAPHIC_VARIABLES

    ps = []

    age = demographic_data[:, AGE_IDX]
    n = len(age)

    for i in range(n_measure):

        y = demographic_data[:, N_DEMOGRAPHIC_VARIABLES + i]

        cor, p = scipy.stats.pearsonr(
            age,
            y
        )

        print(f'Pearson corr age - measure {i}: $r_pearson={cor:.2f}$, $p={p:.3f}$, $n={n}$')

        print()
        ps.append(p)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01, method="b")

    print("p_corrected = ", [f"{i:.3f}" for i in p_corr])
    print()


def get_demographic_data():

    users = User.objects.all().order_by('id')
    age = [u.age for u in users]
    gender = [0 if u.gender == 'male' else 1 for u in users]
    n = len(age)

    demographic_data = np.zeros((n, 4))  # Suppose gender, age, measure 1, measure 2
    demographic_data[:, GENDER_IDX] = gender
    demographic_data[:, AGE_IDX] = age
    demographic_data[:, 2] = np.random.random(n)
    demographic_data[:, 3] = np.random.random(n)
    return demographic_data


def ad_hoc():

    demographic_data = get_demographic_data()

    _stats_age(demographic_data)
    _figure_age(demographic_data)

    _stats_gender(demographic_data)
    _figure_gender(demographic_data)
