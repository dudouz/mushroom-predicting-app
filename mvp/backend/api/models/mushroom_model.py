from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mushroom(Base):
    __tablename__ = 'mushrooms'

    id = Column(Integer, primary_key=True)
    cap_shape = Column(String)
    cap_surface = Column(String)
    cap_color = Column(String)
    bruises = Column(String)
    odor = Column(String)
    gill_attachment = Column(String)
    gill_spacing = Column(String)
    gill_size = Column(String)
    gill_color = Column(String)
    stalk_shape = Column(String)
    stalk_root = Column(String)
    stalk_surface_above_ring = Column(String)
    stalk_surface_below_ring = Column(String)
    stalk_color_above_ring = Column(String)
    stalk_color_below_ring = Column(String)
    veil_type = Column(String)
    veil_color = Column(String)
    ring_number = Column(String)
    ring_type = Column(String)
    spore_print_color = Column(String)
    population = Column(String)
    habitat = Column(String)