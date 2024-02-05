import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import matplotlib.pyplot as plt
import numpy as np


def get_data(video_id):
    data = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    df = pd.DataFrame(data)
    compList = list(df['text'].str.split(" "))

    # complist to lower
    compList = [[x.lower() for x in sublist] for sublist in compList]

    flatList = [item for sublist in compList for item in sublist]
    wordsDF = pd.DataFrame(flatList, columns=['words'])
    conteo = wordsDF.words.value_counts().to_frame()
    return conteo


def filterDataEsp(df):

    filt = 'que de la y en el a los un es las se por lo con del nos una como al'
    filt += ' más esto este está al eso hay ha su les porque esta son cada sin me'
    filt += ' sus ser ese cómo han qué acá estas allí va ahí mi aquí o le esa para'
    filt_list_1 = filt.split()

    filt_list = [
    "a", "al", "algo", "ante", "como", "con", "cual", "cuando", "de", "del", "desde", "donde",
    "durante", "e", "en", "entre", "era", "erais", "eran", "eras", "eres", "es", "esa", "esas", "ese",
    "eso", "esos", "esta", "estabais","estabas", "estad", "estada", "estadas", "estamos",
    "estando", "estar", "estaremos", "estará", "estarán", "estarás", "estaré", "estaréis", "estaría", "estaríais", "estaríamos",
    "estarían", "estarías", "estas", "este", "estemos", "esto", "estos", "estoy", "estuve", "estuviera", "estuvierais", "estuvieran",
    "estuvieras", "estuvieron", "estuviese", "estuvieseis", "estuviesen", "estuvieses", "estuvimos", "estuviste", "estuvisteis",
    "estuviéramos", "estuviésemos", "estuvo", "está", "estábamos", "estáis", "están", "estás", "esté", "estéis", "estén", "estés",
    "fue", "fuerais", "fueran", "fueras", "fueron", "fuese", "fueseis", "fuesen", "fueses", "fui", "fuimos", "fuiste",
    "fuisteis", "fuéramos", "fuésemos", "ha", "habida", "habidas", "habido", "habidos", "habiendo", "habremos",
    "habrás", "habré", "habréis", "habría", "habríais", "habríamos", "habrían", "habrías", "habéis", "había", "habíais", "habíamos",
    "habías", "han", "has", "hasta", "hayamos", "hayan", "hayas", "hayáis", "he", "hemos", "hube", "hubiera",
    "hubierais", "hubieran", "hubieras", "hubiese", "hubieseis", "hubiesen", "hubieses", "hubimos", "hubiste",
    "hubisteis", "hubiéramos", "hubiésemos", "la", "las", "le", "les", "lo", "los", "me", "mi", "mis",
    "muy", "más", "mí", "ni", "nos", "o", "os", "por", "porque", "que", "qué", "se", "sea", "seas", "seremos", "será", "serás", "seré", "seréis", "sería",
    "seríais", "serías", "seáis", "sido", "siendo", "sois", "somos", "son", "su",
    "sus", "suya", "suyas", "suyo", "suyos", "también", "tanto", "te", "ti", "tiene", "tienen", "tienes", "tu", "tus", "tuve", "tuviera", "tuvierais", "tuvieran",
    "tuvieras", "tuvieron", "tuviese", "tuvieseis", "tuviesen", "tuvieses", "tuvimos", "tuviste", "tuvisteis", "tuviéramos",
    "tuviésemos", "tuvo", "tuya", "tuyas", "tuyo", "tuyos", "tú", "un", "una", "uno", "unos", "vosotras", "vosotros", "vuestra",
    "vuestras", "vuestro", "vuestros", "y", "ya", "éramos"
]
    filt_list.extend(['eh', 'y', 'va', 'se', 'como'])
    filt_list.extend(filt_list_1)

    # filt_list to lower
    filt_list = [x.lower() for x in filt_list]

    ret = df[~df.index.isin(filt_list)]

    return ret


def graf_1(df, n=30, titulo='Word Frequency'):
    df = df.head(n)
    plt.style.use('dark_background')

    # Normalize count values to map to the colormap
    norm = plt.Normalize(df['count'].min(), df['count'].max())
    colors = plt.cm.viridis(norm(df['count']))  # viridis is a colormap, you can choose others like inferno, magma, etc.

    # Plotting with color intensity based on count
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df.index, df['count'], color=colors)

    # Adding a colorbar to show the mapping from color intensity to count values
    sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Count Intensity')

    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title(titulo)
    plt.xticks(rotation=75)

    return plt


def graf_2(df, n=30, titulo='Word Cloud'):
    df = df.head(n)
    plt.style.use('dark_background')

    # Normalize counts to determine font size and colors
    max_size = 70  # Max font size
    min_size = 10  # Min font size
    words = df.index
    counts = df['count']

    # Create sizes and colors for each word
    sizes = [min_size + (max_size - min_size) * (count / max(counts)) for count in counts]
    colors = plt.cm.viridis(np.linspace(0, 1, len(words)))  # Use a colormap
    # Create a scatter plot to get a layout that avoids overlap (optional)
    x = np.random.rand(len(words))
    y = np.random.rand(len(words))
    fig, ax = plt.subplots(figsize=(12, 8))
    # Plot each word. Adjust the positions to make sure words don't overlap much.
    for i, word in enumerate(words):
        ax.text(x[i], y[i], word, fontsize=sizes[i], color=colors[i], ha='center', va='center', alpha=0.7)
    # Remove axes and ticks
    ax.set_axis_off()
    # Add title and possibly a custom legend or colorbar here if desired
    plt.title(titulo)

    return plt

