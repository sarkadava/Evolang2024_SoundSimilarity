# sound_similarity

This folder contains 
1. folder 'data' - containing original audio for an event, as well as cutted events to segments (not pushed to Github)
2. folder 'datasets' - containing all the datasets that have been used to make plots (or can be potentially used to do stats)
        - distance_matrix: matrix of distances between a segment and all other segments
        - segments_soundgen_summary_new: ouput of soundgen() function
        - umap_df - dataset of concepts and their coordinates in reduced 2-dimensional space
        - meanDist_pertrial: complete dataset with all metadata, used features, plus mean calculated from 'distance_matrix' within a trial (i.e., concrete realization of a concept by a participant)
        - meanDist_perpcn: complete dataset with all metadata, used features, plus mean calculated from 'distance_matrix' within a participant (ignoring trial differentiation)
    3. folder 'plots'
    4. Python script to cut audio to segments
    5. Rmd with
        - soundgen()
        - umap reduction
        - distance matrix
        - plot generation