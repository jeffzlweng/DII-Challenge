p_dict = {}
model_file = "/Users/Andy/Documents/GitHub/DII-Challenge/data/models/task1-snm-5-snr-3-value-1-trend-1-cat-1-lt--4-size-256-seed-1-best.ckpt"

load_model(p_dict, model_file)

all_dict = torch.load(model_file)
