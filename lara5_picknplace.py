from neurapy.robot import Robot
import time
from enum import Enum

r = Robot()
SPEED = 2
ACC = 1
BLEND_RAD = 0.005

# Koords für Anker UL: [0.23324642299354773, 0.26552352811667407, 0.2706854467560163, -0.001592390580589725, 3.1354401423367158, 1.1574626574404814]
# Koords für Anker UR: [0.23536904643142453, 0.33349096254770777, 0.26931403641827756, -0.0012799971994688108, 3.1359847488470476, 1.1576595456033432]

# Koords für Anker ML: [0.16667606070572483, 0.26538717386696803, 0.2700166407501304, -0.0013609491889034178, 3.1357888683100947, 1.1575864046451678]
# Koords für Anker MR: [0.16724577917119232, 0.33441732116260225, 0.2694421745067921, -0.0011502240711528933, 3.136148849381651, 1.1577280033570876]

# Koords für Anker OL: [0.09856443314783316, 0.2669544349488446, 0.2696519840366448, -0.001291972675888471, 3.1357318367896583, 1.1576046697361353]
# Koords für Anker OR: [0.09990713489385245, 0.3352316879600828, 0.269835240436353, -0.0009910986937195184, 3.13628853790317, 1.1578024091380712]




# Koords für Anker in Topf (jeweils groß), UL Feld: [0.19296557005685952, -0.36311403165524314, 0.2736523450962862, -3.132603703517428, 0.007004878724304366, 2.7320647763196884]
# Koords für Anker in Topf UR: [0.19451548975354624, -0.2635331410150363, 0.27389204446409037, -3.132574989062524, 0.007006367913658484, 2.7320739575095123]

# Koords für Anker in Topf ML: [0.11341278484260371, -0.36261522780594324, 0.27368236737125284, -3.132651984145072, 0.006999241173476595, 2.732064571884557]
# Koords für Anker in Topf MR: [0.1157969932005576, -0.26220635056902536, 0.2739386178855886, -3.1351560761623096, 0.003602776599224449, 2.7320987854479912]

# Koords dür Anker in Topf OL: [0.033002659942211174, -0.36057207551440723, 0.27349325367087696, -3.132724640420551, 0.006800271018250902, 2.7321314047118035]
# Koords für Anker in Topf OR: [0.03571620487072412, -0.26065542658565893, 0.27465568920307504, -3.132781297044438, 0.006594387465330453, 2.7321899060279535]

coord_dict = {
        
    "ABL" : [0.23324642299354773, 0.26552352811667407, 0.2706854467560163, -0.001592390580589725, 3.1354401423367158, 1.1574626574404814], #bottom left
    "ABR" : [0.23536904643142453, 0.33349096254770777, 0.26931403641827756, -0.0012799971994688108, 3.1359847488470476, 1.1576595456033432],

    "AML" : [0.16667606070572483, 0.26538717386696803, 0.2700166407501304, -0.0013609491889034178, 3.1357888683100947, 1.1575864046451678],
    "AMR" : [0.16724577917119232, 0.33441732116260225, 0.2694421745067921, -0.0011502240711528933, 3.136148849381651, 1.1577280033570876], # TODO

    "ATL" : [0.09856443314783316, 0.2669544349488446, 0.2696519840366448, -0.001291972675888471, 3.1357318367896583, 1.1576046697361353],
    "ATR" : [0.09990713489385245, 0.3352316879600828, 0.269835240436353, -0.0009910986937195184, 3.13628853790317, 1.1578024091380712],

    "TBL" : [0.19296557005685952, -0.36311403165524314, 0.2736523450962862, -3.132603703517428, 0.007004878724304366, 2.7320647763196884], #bottom left
    "TBR" : [0.19451548975354624, -0.2635331410150363, 0.27389204446409037, -3.132574989062524, 0.007006367913658484, 2.7320739575095123],

    "TML" : [0.11341278484260371, -0.36261522780594324, 0.27368236737125284, -3.132651984145072, 0.006999241173476595, 2.732064571884557],# TODO
    "TMR" : [0.1157969932005576, -0.26220635056902536, 0.2739386178855886, -3.1351560761623096, 0.003602776599224449, 2.7320987854479912],

    "TTL" : [0.033002659942211174, -0.36057207551440723, 0.27349325367087696, -3.132724640420551, 0.006800271018250902, 2.7321314047118035],
    "TTR" :  [0.03571620487072412, -0.26065542658565893, 0.27465568920307504, -3.132781297044438, 0.006594387465330453, 2.7321899060279535],

}

def move_to_coord(coordinates):

    trajectory = get_linear_property(coordinates)
    
    
    r.move_linear_from_current_position(**trajectory)
    time.sleep(0.5)
    r.stop()
    
def gripp_anker(coordinates):

    #move above anker 
    coordinates[2] += 0.2
    move_to_coord(coordinates)

    #move to anker 
    coordinates[2] -= 0.2
    move_to_coord(coordinates)

    r.gripper('off')

    coordinates[2] += 0.2
    move_to_coord(coordinates)

    r.stop()
   
def place_anker(coordinates):

    #move above topf 
    coordinates[2] += 0.2
    move_to_coord(coordinates)

    #move to topf 
    coordinates[2] -= 0.2
    move_to_coord(coordinates)

    r.gripper('on')

    coordinates[2] += 0.2
    move_to_coord(coordinates)

    r.stop()

def get_linear_property(coordinates):

    linear_property = {
        "speed": SPEED,
        "acceleration": ACC,
        "blend_radius": BLEND_RAD,
        "target_pose": [
            coordinates
        ],
    "current_joint_angles":r.robot_status("jointAngles")
    }

    return linear_property

def set_gripper_tool(name):
    
    tool_data = { '_controlOA': False,
    '_controlOD': False,
    '_toolOA': False,
    '_toolOD': True,
    'autoM': 2,
    'autoMeasureX': 0,
    'autoMeasureY': 0,
    'autoMeasureZ': 0,
    'closeInput': 40,
    'cmdID': 16,
    'description': 'Tool Description',
    'force': 50,
    'gripper': '',
    'grippertype': 'Standard Gripper',
    'inertiaXX': 0,
    'inertiaXY': 0,
    'inertiaXZ': 0,
    'inertiaYY': 0,
    'inertiaYZ': 0,
    'inertiaZZ': 0,
    'name': f'{name}',
    'offCOA': [0, 0, 0, 0, 0, 0, 0, 0],
    'offCOD1': 0,
    'offCOD2': 0,
    'offTOA': [0, 0],
    'offTOD': 1,
    'offsetA': 0,
    'offsetB': 0,
    'offsetC': 0,
    'offsetX': 0,
    'offsetY': 0,
    'offsetZ': 0,
    'onCOA': [0, 0, 0, 0, 0, 0, 0, 0],
    'onCOD1': 0,
    'onCOD2': 0,
    'onTOA': [0, 0],
    'onTOD': 2,
    'openInput': 40,
    'portID': '',
    'protocol': 0,
    'robot_type': 'Tool',
    'slaveID': 0,
    'speed': 50}

    tools_data = r.create_tool(tool_data)
    r.set_tool(tool_name = name)

def move_above_object(coordinates):

    #move above topf 
    coordinates[2] += 0.2
    move_to_coord(coordinates)

    #move to topf 
    #coordinates[2] -= 0.2
    #move_to_coord(coordinates)

    r.stop()

def main():

    keys = ["ABL", "ABR", "AML", "AMR", "ATL", "ATR"]
    keys_topf = ["TBL", "TBR", "TML", "TMR", "TTL", "TTR"]

    for i,_ in enumerate(keys):
        gripp_anker(coord_dict[keys[i]])
        place_anker(coord_dict[keys_topf[i]])
    

if _name=="main_":
    main()