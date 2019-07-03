import os

FIG_FOLDER = os.path.join("fig", "main")
SUP_FIG_FOLDER = os.path.join("fig", "sup")
os.makedirs(FIG_FOLDER, exist_ok=True)
os.makedirs(SUP_FIG_FOLDER, exist_ok=True)

AGENT_LABELLING = {
    3:
        {
            0: '$(3, 1)$',
            1: '$(1, 2)$',
            2: '$(2, 3)$',
        },
    4: {
            0: '$(4, 1)$',
            1: '$(1, 2)$',
            2: '$(2, 3)$',
            3: '$(3, 4)$'
        }
}
