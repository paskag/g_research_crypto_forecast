def config_rf(name):
    configs = {
        "Bitcoin": {'max_depth': 3, 'max_features': 'log2', 'n_estimators': 50, "criterion": "absolute_error"},
        "Bitcoin Cash": {'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 100, "criterion": "absolute_error"},
        "Binance Coin": {'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 100, "criterion": "absolute_error"},
        "EOS_IO": {'max_depth': 3, 'max_features': 'log2', 'n_estimators': 50, "criterion": "absolute_error"},
        "Ethereum Classic": {'max_depth': 3, 'max_features': 'log2', 'n_estimators': 50, "criterion": "absolute_error"},
        "Ethereum": {'max_depth': 3, 'max_features': 'log2', 'n_estimators': 50, "criterion": "absolute_error"},
        "Litecoin": {'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50, "criterion": "absolute_error"},
        "Monero": {'max_depth': 3, 'max_features': 'log2', 'n_estimators': 50, "criterion": "absolute_error"}
    }
    return configs[name]


def config_svr(name):
    configs = {
        "Bitcoin": {'C': 2.5, 'gamma': 'scale', 'kernel': 'linear'},
        "Bitcoin Cash": {'C': 2.0, 'gamma': 'scale', 'kernel': 'linear'},
        "Binance Coin": {'C': 0.5, 'gamma': 'auto', 'kernel': 'rbf'},
        "EOS_IO": {'C': 1.5, 'gamma': 'scale', 'kernel': 'linear'},
        "Ethereum Classic":{'C': 2.5, 'gamma': 'scale', 'kernel': 'linear'},
        "Ethereum": {'C': 0.5, 'gamma': 'auto', 'kernel': 'poly'},
        "Litecoin": {'C': 2.5, 'gamma': 'scale', 'kernel': 'linear'},
        "Monero": {'C': 2.0, 'gamma': 'scale', 'kernel': 'linear'}
    }
    return configs[name]


def config_xgb(name):
    configs = {
        "Bitcoin": {'max_depth': 3, 'n_estimators': 50},
        "Bitcoin Cash": {'max_depth': 3, 'n_estimators': 50},
        "Binance Coin": {'max_depth': 3, 'n_estimators': 50},
        "EOS_IO": {'max_depth': 7, 'n_estimators': 50},
        "Ethereum Classic": {'max_depth': 3, 'n_estimators': 50},
        "Ethereum": {'max_depth': 3, 'n_estimators': 50},
        "Litecoin": {'max_depth': 3, 'n_estimators': 50},
        "Monero": {'max_depth': 3, 'n_estimators': 50}
    }
    return configs[name]


def main():
    test = config_rf("Bitcoin")
    print(test)


if __name__ == "__main__":
    main()
