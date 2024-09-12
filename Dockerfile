name: "ai_u2net_color_clustering"
author: Suxing Liu
public: True
clone: True
image: docker://computationalplantscience/ai_u2net_color_clustering
commands: /opt/smart/plantit_pipeline.sh

input:
  kind: directory
  path:
  filetypes:
    - jpg
    - png
    
output:
  path:
  include:
    patterns:
      - png
      
logo: media/rosette.jpg

jobqueue:
  walltime: "01:00:00"
  memory: "16GB"
  processes: 1
  cores: 12
