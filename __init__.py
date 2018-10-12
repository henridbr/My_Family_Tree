# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft_family_learning

# Mycroft libraries

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler


import requests
import json

__author__ = 'henridbr' # hd@uip

LOGGER = getLogger(__name__)


class FamilyLearningSkill(MycroftSkill):

    def __init__(self):
        super(FamilyLearningSkill, self).__init__(name="FamilyLearningSkill")
        
    @intent_handler(IntentBuilder("FamilyLearningIntent").require("FamilyLearningKeyword"))
    def handle_family_learning_intent(self, message):
        self.speak_dialog("save.it.memory")

        
##### Son
    @intent_handler(IntentBuilder("SonIntent").require("SonKeyword"))
    def handle_son_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)

        membersname = family['family_dictionary']['members']
        
        namelist = []
        namegroup = ""
        
        i=0
        while i< len(membersname):
            if (membersname[i]['rank'] == "son"):
                namelist.append(membersname[i]['first_name'])
            i = i+1
        i=1
        if len(namelist) ==0 :
            self.speak_dialog('you have no son')
        elif len(namelist) ==1 :
            self.speak_dialog(namelist[0] + " is your son")            
        else:
            namegroup = namelist[0]
            while i< len(namelist):
                namegroup = namegroup +" and " + namelist[i]
                i = i+1
            self.speak_dialog('{} are your sons'.format(namegroup))
     
        
##### Daughter
    @intent_handler(IntentBuilder("DaughterIntent").require("DaughterKeyword"))
    def handle_daughter_intent(self, message):
           
        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)

        membersname = family['family_dictionary']['members']

        namelist = []
        namegroup = ""
        
        i=0
        while i< len(membersname):
            if (membersname[i]['rank'] == "daughter"):
                namelist.append(membersname[i]['first_name'])
            i = i +1
        i=1
        if len(namelist) ==0 :
            self.speak_dialog('you have no daughter')
        elif len(namelist) ==1 :
            self.speak_dialog(namelist[0] + " is your daughter")            
        else:
            namegroup = namelist[0]
            while i< len(namelist):
                namegroup = namegroup +" and " + namelist[i]
                i = i+1
            self.speak_dialog('{} are your daughters'.format(namegroup))

        
        
##### Grand Son
    @intent_handler(IntentBuilder("GrandSonIntent").require("GrandSonKeyword"))
    def handle_grand_son_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)

        membersname = family['family_dictionary']['members']

        namelist = []
        namegroup = ""
        
        i=0
        while i< len(membersname):
            if (membersname[i]['rank'] == "grand_son"):
                namelist.append(membersname[i]['first_name'])
            i = i +1
        i=1
        if len(namelist) ==0 :
            self.speak_dialog('you have no grand son')
        elif len(namelist) ==1 :
            self.speak_dialog(namelist[0] + " is your grand son")            
        else:
            namegroup = namelist[0]
            while i< len(namelist):
                namegroup = namegroup +" and " + namelist[i]
                i = i+1
            self.speak_dialog('{} are your grand sons'.format(namegroup))

        
##### Grand Daughter
    @intent_handler(IntentBuilder("GrandDaughterIntent").require("GrandDaughterKeyword"))
    def handle_grand_daughter_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)

        membersname = family['family_dictionary']['members']

        namelist = []
        namegroup = ""
        
        i=0
        while i< len(membersname):
            if (membersname[i]['rank'] == "grand_daughter"):
                namelist.append(membersname[i]['first_name'])
            i = i +1
        i=1
        if len(namelist) ==0 :
            self.speak_dialog('you have no grand daughter')
        elif len(namelist) ==1 :
            self.speak_dialog(namelist[0] + " is your grand daughter")            
        else:
            namegroup = namelist[0]
            while i< len(namelist):
                namegroup = namegroup +" and " + namelist[i]
                i = i+1
            self.speak_dialog('{} are your grand daughters'.format(namegroup))

            
#### Living Place
    @intent_handler(IntentBuilder("LivingPlaceIntent").require("LivingPlaceKeyword").require("FamilyFirstName"))
    def handle_living_place(self, message):
  
        member = message.data.get('FamilyFirstName')
        print(member)
        member = member.capitalize()
               
        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)

        membersname = family['family_dictionary']['members']

        memberslivingplace ={}

        i=0
        while i< len(membersname):
            who = membersname[i]['first_name']
            where = membersname[i]['location']
            memberslivingplace[who] = where
            i = i +1

        livingplace = memberslivingplace[member]
 
        self.speak('{} is from {}'.format(member, livingplace))
            
            
    
    def stop(self):
        pass

def create_skill():
    return FamilyLearningSkill()
