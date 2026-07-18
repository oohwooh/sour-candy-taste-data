# Radar graph for sour patch
import numpy as np
import matplotlib.pyplot as plt

def radar(candy_data, CANDY_NAME):
  CATEGORIES = ['Sour Branding (Submit BEFORE eating the candy)', 'Sour Intensity', 'Sour Duration', 'Mouth Feel']
  LABELS = ['Sour Branding', 'Sour Intensity', 'Sour Duration', 'Mouth Feel']

  responses = candy_data[CANDY_NAME]

  individual_values = []
  for response in responses:
      values = [float(response[category]) for category in CATEGORIES]
      individual_values.append(values)

  averages = []
  for category in CATEGORIES:
      values = [float(response[category]) for response in responses if response[category]]
      averages.append(sum(values) / len(values))

  angles = np.linspace(0, 2 * np.pi, len(CATEGORIES), endpoint=False).tolist()
  angles += angles[:1]

  fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

  for i, values in enumerate(individual_values):
      values = values + values[:1]
      line, = ax.plot(angles, values, linewidth=1, linestyle='--', alpha=0.5, label=f'Response {i + 1}')
      # ax.fill(angles, values, alpha=0.1, color=line.get_color())

  averages += averages[:1]
  ax.plot(angles, averages, 'o-', linewidth=2, color='blue', label='Average')
  ax.fill(angles, averages, alpha=0.5, color='blue')

  ax.set_thetagrids(np.degrees(angles[:-1]), LABELS)
  ax.set_ylim(0, 5)
  ax.set_title(CANDY_NAME)
  ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

  plt.show()
