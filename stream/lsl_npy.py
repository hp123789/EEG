from pylsl import StreamInlet, resolve_stream
import time
import numpy as np

streams = resolve_stream('type', 'EEG')

data = []
t_end = time.time() + 7

inlet = StreamInlet(streams[0])

while 1:
    sample, timestamp = inlet.pull_sample()
    if sample:
        data.append(sample)
        if len(data) > 1250:
            data.pop(0)
            a = np.array(data)
            np.save("eegdata", a)