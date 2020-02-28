from __future__ import print_function

from keras.callbacks import ModelCheckpoint

from data import load_train_data
from utils import *

create_paths()
log_file = open(global_path + "logs/log_file.txt", 'a')

# CEAL data definition
X_train, y_train = load_train_data()
labeled_index = np.arange(0, nb_labeled)
unlabeled_index = np.arange(nb_labeled, len(X_train))

# (1) Initialize model
model = get_unet(dropout=True)

model_checkpoint = ModelCheckpoint(final_weights_path, monitor='loss', save_best_only=True)

history = model.fit(X_train[labeled_index], y_train[labeled_index], batch_size=2, nb_epoch=nb_initial_epochs,
                    verbose=1, shuffle=True, callbacks=[model_checkpoint])

model.save(global_path + "models/active_model.h5")
log(history, 0, log_file)

log_file.close()
