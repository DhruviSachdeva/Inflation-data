from macrodata_tools.data import get_cpi, compute_inflation, inflation_summary, plot_inflation

# download CPI
cpi = get_cpi()

# compute inflation
inflation = compute_inflation(cpi)

# print summary statistics
print(inflation_summary(inflation))

# plot inflation
plot_inflation(inflation)