from matplotlib import pyplot as plt

def grafico_scatole_spezzato (df,lblx,lbly,ybrake,ystart,ratio,fontsize = 20,labelsize = 18,title = '',top = 0.87,ymin = 0,put_double_ylbl = True):
    fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True,facecolor='w',gridspec_kw={'height_ratios': ratio})
    ax1.boxplot(df)
    ax1.set_xlabel('')
    ax1.tick_params(length = 0)
    ax1.set_ylim(ymin = ystart)
    ax1.tick_params(labelsize = labelsize)
    fig.suptitle(title, fontsize=fontsize)
    if put_double_ylbl:
        ax1.set_ylabel (lbly,fontsize=fontsize)
    ax2.set_ylabel (lbly,fontsize=fontsize)
    ax1.spines['bottom'].set_visible(False)
    ax2.boxplot(df)
    ax2.set_title('')
    ax2.set_ylim(ymin,ybrake)
    fig.subplots_adjust(top=top)

    ax2.tick_params(length = 0,labelsize = labelsize)
    ax2.set_xlabel(lblx,fontsize=fontsize)
    ax2.spines['top'].set_visible(False)
    return fig