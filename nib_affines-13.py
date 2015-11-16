output_shape = (5, 6, 7)
i_coords, j_coords, k_coords = np.meshgrid(range(output_shape[0]), range(output_shape[1]), range(output_shape[2]),
                                           indexing='ij')
coordinate_grid = np.array([i_coords, j_coords, k_coords])
coordinate_grid.shape
# (3, 5, 6, 7)
