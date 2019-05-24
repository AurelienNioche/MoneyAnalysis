import matplotlib.pyplot as plt


def plot(mean, std, cond='', n_good='', agent_type=''):

    fig = plt.figure(figsize=(15, 12))
    ax = fig.subplots()

    ax.plot(mean, lw=1.5)
    ax.fill_between(
        range(len(mean)),
        y1=mean - std,
        y2=mean + std,
        alpha=0.5
    )

    ax.spines['right'].set_visible(0)
    ax.spines['top'].set_visible(0)
    ax.set_xlabel('trials')
    ax.set_ylabel('p(choose ind. ex. with good 0)')

    plt.title(f'{n_good} - {cond} - type{agent_type}')
    f_name = f"fig/learning_curves_{n_good}_{cond}_{agent_type}.pdf"
    plt.savefig(f_name)
    print(f'{f_name} has been produced')
    plt.close()
