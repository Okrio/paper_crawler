## 2023-08-17
|type|paper|abstract|url|author|
|---|---|---|---|---|
|SPEECH_ENHANCEMENT|speech enhancement using ego-noise references with a microphone array embedded in an unmanned aerial vehicle|a method is proposed for performing speech enhancement using ego-noise references with a microphone array embedded in an unmanned aerial vehicle (uav). the ego-noise reference signals are captured with microphones located near the uav's propellers and used in the prior knowledge multichannel wiener filter (pk-mwf) to obtain the speech correlation matrix estimate. speech presence probability (spp) can be estimated for detecting speech activity from an external microphone near the speech source, providing a performance benchmark, or from one of the embedded microphones, assuming a more realistic scenario. experimental measurements are performed in a semi-anechoic chamber, with a uav mounted on a stand and a loudspeaker playing a speech signal, while setting three distinct and fixed propeller rotation speeds, resulting in three different signal-to-noise ratios (snrs). the recordings obtained and made available online are used to compare the proposed method to the use of the standard multichannel wiener filter (mwf) estimated with and without the propellers' microphones being used in its formulation. results show that compared to those, the use of pk-mwf achieves higher levels of improvement in speech intelligibility and quality, measured by stoi and pesq, while the snr improvement is similar.|https://arxiv.org/abs/2211.02690|['elisa tengan', 'thomas dietzen', 'santiago ruiz', 'mansour alkmim', 'joão cardenuto', 'toon van waterschoot']|
|SPEECH_SEPARATION|scanet: a self- and cross-attention network for audio-visual speech separation|the integration of different modalities, such as audio and visual information, plays a crucial role in human perception of the surrounding environment. recent research has made significant progress in designing fusion modules for audio-visual speech separation. however, they predominantly focus on multi-modal fusion architectures situated either at the top or bottom positions, rather than comprehensively considering multi-modal fusion at various hierarchical positions within the network. in this paper, we propose a novel model called self- and cross-attention network (scanet), which leverages the attention mechanism for efficient audio-visual feature fusion. scanet consists of two types of attention blocks: self-attention (sa) and cross-attention (ca) blocks, where the ca blocks are distributed at the top (tca), middle (mca) and bottom (bca) of scanet. these blocks maintain the ability to learn modality-specific features and enable the extraction of different semantics from audio-visual features. comprehensive experiments on three standard audio-visual separation benchmarks (lrs2, lrs3, and voxceleb2) demonstrate the effectiveness of scanet, outperforming existing state-of-the-art (sota) methods while maintaining comparable inference time.|https://arxiv.org/abs/2308.08143|['kai li', 'runxuan yang', 'xiaolin hu']|
