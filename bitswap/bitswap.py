# async imports

# import decision_engine
# import stats
# import types
# import want_manager

# import constants
# import network
# import notifications
# from log import log


default_options = {
    'statsEnabled': False,
    'statsComputeThrottleTimeout': 1000,
    'statsComputeThrottleMaxQueueSize': 1000
}
statsKeys = [
    'blocksReceived',
    'dataReceived',
    'dupBlksReceived',
    'dupDataReceived',
    'blocksSent',
    'dataSent',
    'providesBufferLength',
    'wantListLength',
    'peerCount'
]
