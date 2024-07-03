class Artifact:
  def __init__(self, name, origin):
    self.name = name
    self.origin = origin
    self.materials = []

  def add_material(self, material):
    self.materials.append(material)

  def remove_material(self, material):
    if material in self.materials:
      self.materials.remove(material)
    else:
      print(f"Material '{material}' not found in artifact '{self.name}'.")

  def display_materials(self):
    if not self.materials:
      print(f"Artifact '{self.name}' has no materials listed.")
    else:
      print(f"Artifact: {self.name} ({self.origin})")
      print(f"Materials:")
      for material in self.materials:
        print(f"- {material}")

def find_artifact_with_most_materials(artifacts):
  most_materials = 0
  artifact_with_most = None
  for artifact in artifacts:
    if len(artifact.materials) > most_materials:
      most_materials = len(artifact.materials)
      artifact_with_most = artifact
  return artifact_with_most

# Example usage
artifact1 = Artifact("Golden Scarab", "Egyptian")
artifact2 = Artifact("Roman Coin", "Roman")
artifact3 = Artifact("Clay Tablet", "Mesopotamian")

artifact1.add_material("Lapis Lazuli")
artifact2.remove_material("Silver")  # This material wasn't there

artifact1.display_materials()
artifact2.display_materials()
artifact3.display_materials()

most_material_artifact = find_artifact_with_most_materials([artifact1, artifact2, artifact3])
print(f"\nArtifact with the most materials:")
most_material_artifact.display_materials()
