from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the Unicode art as a multiline string
western_bluebird = """
              ▄▖▘▀▀▀▝▘▘▄                                    
            ▗▛▘         ▀▖                                  
           ▗▛▗▖▖ ▞▄     ▄▐                                  
          ▗▀▖   ▝▀▀▗  ▗▀▘ ▄▚                                
         ▗▌ ▚     ▖    ▄▛▚▖                                 
         ▙▙ ▝▛ ▖▘▗▖▖▘▗   ▐▝                                 
       ▄▀      ▝ ▗▄▄▄▘▐  ▜▌                                 
       ▟           ▝  ▗▘▀▀▀▄▖                               
      ▗▛▘                   ▜▄                              
      ▞   ▞     ▗            ▝▜▖                            
     ▗█▘ ▞       ▖ ▝           ▝▄                           
     ▝▞ ▐        ▝▖  ▘      ▝    ▚                          
      ▌            ▜▖ ▝▗ ▘   ▙   ▝▚                         
 ▖    ▖             ▝▀▄  ▄▞    ▘▖ ▀▚▖                       
  ▘▗  ▜                ▀▚  ▝▘▖  ▝   ▝▄                      
    ▝▖▝  ▗▖ ▗            ▀▗▖ ▝▀▘      ▚                     
      ▀▌ ▐▌                ▝▚▖  ▝▗  ▖  ▝▖                   
       ▝▖▘▌  ▘       ▗       ▝▜▄ ▘ ▗ ▗  ▀▖                  
   ▘▖   ▝▟▚   ▝▙               ▝▚▖ ▘▞▗▝▗▖▚                  
     ▘▖  ▝▀▌    ▝▖      ▝▀ ▄▄▄   ▝▚▖ ▝▝█▄▙▙                 
       ▘▖  ▝▄▄▄   ▘▖               ▝▀▄▖  ▀▀▙                
         ▚ ▖▟▜██▖   ▘ ▄  ▝            ▞▀▄▖  ▀▄              
          ▝▌     ▀▄▖  ▖ ▟▘ ▝▘▗▄▄▄▖    ▗ ▖▝▀▗▄▝▙▖            
            ▗       ▀▜▛▀█▞▀▝▗▟▌▖ ▗▄  ▄▖▀▗▘▖  ▀▘█            
              ▖       ▘     ▗▜  ▝▗▖▀ ▄▗▄▘▀▗▘▄ ▝▄▘▖          
              ▝▗       ▘▖   ▛▌    ▝▘▄ ▝▀▛▄▄▞▚▞▗ ▝▄▚         
                ▘▖       ▘▖▟▐▌       ▀▄▖ ▘▖▝▀▀▙▞▘▖▝▜▄       
                 ▐▄  ▗▄▟▟█▘▘▞          ▝▚▖▝▚▖  ▝▚▞▀▄▝▀▖     
                  ▘▖ ▝  ▗▗▞▐▀▟           ▝▚▖▝▄   ▝▀▄▝▀█▌    
                   ▝▗  ▝▖▜ ▌  ▘            ▝▚▖▚▖    ▀▄▖▀▙▖  
                     ▝▖▖▐ ▀▖    ▗            ▝▚▞▖     ▀▙█▘  
                       ▜▞        ▝▗            ▀█        ▘  
                        ▀▗         ▝▗▖                      
                          ▝▖          ▘▄                    
"""

northern_cardinal = """
          ▗▖                                                
         ▗▗▛                                                
        ▗▘ ▜                                                
       ▞   ▝▌                                               
     ▗▝    ▝▘▖                                              
    ▞        ▗                                              
  ▗▀▛▄▄▖▚▄    ▝▖                                            
▗▝  ▜▄ ▗▀      ▝▖                                           
▘▚▀▀▝▐▖▞        ▙                                           
   ▛▚▀▜         ▐▙▗                                         
   ▚  ▌        ▝▀  ▝ ▖                                      
   ▝▚▟▘               ▘▗                                    
    ▞         ▄▄         ▘▘▖                                
    ▌          ▝▀▌▗▖        ▝ ▖                             
    ▗            ▐  ▝▀▀▀▀▝     ▘▗                           
    ▗             ▚    ▖   ▗▄▄▖  ▝▗                         
     ▖            ▝▖▝▘▘ ▗ ▝▘▖▘     ▝▖                       
     ▝▗            ▝▗▖▞ ▖▄▄          ▚                      
       ▚              ▝▚▝             ▝▄▗   ▗               
        ▝▗              ▀▗▗▐           ▝▖ ▝▐▙▜▚▀▐▚▌▌▖▖▖     
          ▝▗               ▀▘▘▀▝▗▖  ▖▖ ▖▐▘▘▘ ▗ ▞▝▘▗▗▗▝▝▘▗▗  
            ▝▝▗                 ▗ ▘▘             ▘▘▘▗▘▌▌▘▘▞▄
                ▘▘▄▄▖▖▖▖   ▖▖▖ ▘                        ▝▝  
                  ▘▖     ▀▛▗                                
                 ▞▘       ▝▟                                
                ▟         ▞                                 
              ▗▀         ▞▞                                 
             ▞▞         ▗▝                                  
       ▖▀▝▗▝▘▗         ▗▘▘                                  
      ▘▘▘     ▀▝▘ ▖▖▗▗▗▘▐▗▗ ▖                               
                 ▛  ▘▝     ▘▘▘                              
"""

house_sparrow = """
                                                            
                                                            
                                                            
                                                            
               ▖ ▘▚▘▗                                       
             ▗▘▗▗▗    ▘▖                                    
          ▗▝  ▖ ▀▘▗ ▗  ▝                                    
           ▘▝▐▝▘      ▗▗▝▗                                  
             ▝▖           ▝ ▖                               
              ▌              ▘▖                             
             ▐     ▗▗▗         ▚                            
             ▗      ▖▗ ▄▚▘      ▝▗                          
              ▘   ▝▖             ▚▝▗                        
              ▝▖    ▘▖         ▖    ▝▗                      
                ▚     ▘▗▗▖▖▘▀ ▝ ▖▖▄    ▖                    
                 ▝▗        ▝  ▗▗  ▖ ▝▘ ▝ ▖                  
                   ▝▗              ▝▝▝▗▄▖▖▚▌▖               
                     ▝ ▖            ▝ ▖   ▘▀▗               
                        ▘▗▗▖    ▗▗ ▘▘▝ ▘▘▗▖ ▝▝▖▖            
                       ▗▝▗▘▗▚▀▝            ▘▘▗ ▘▚▖▖         
                   ▄▝▗▚▄▄▖▀▝▖                  ▘ ▖▘▚▖       
                  ▝ ▐▚▚▖   ▚▗▖                    ▝ ▞▝▄     
                                                     ▝▝     
                                                            
                                                            
"""

nuttall_woodpecker ="""
                                                            
                      ▗ ▐▄▄▘  ▗▄▖                           
                    ▗▝▖▝    ▘▐  ▝                           
                  ▗▝▗ ▘ ▗  ▖  ▗  ▖                          
               ▖ ▘  ▝▌ ▀    ▀  ▘ ▗                          
             ▖▘▝     ▀▘▖▄▗▗▖ ▚▄▞                            
           ▗▐▝   ▘       ▗  ▘▞█  ▌                          
          ▗ ▘   ▝    ▝ ▀▘▖▞▙▗▗▖▛▝                           
         ▗▖▘  ▗▝    ▖   ▗▝▌    ▞▝▖                          
        ▗▗    ▘   ▗▝  ▘▐     ▌  ▘▚▖                         
        ▗▘  ▞    ▝  ▝▀▝▗    ▗                               
        ▌  ▝   ▞ ▖▗▘▘  ▗    ▖                               
       ▗▗ ▗   ▗ ▄▖ ▝▝ ▚     ▖                               
       ▗▖ ▖  ▝ ▖ ▖▄ ▖▗      ▛▜                              
       ▌▘   ▌▙▗▖  ▖▙▘▞     ▗ ▝▌▘ ▚              ▗ ▖         
       ▖ ▝ ▞ ▗▗▖▘▘▖▀▛      ▖  ▝                    ▖        
       ▘ ▘▄▝▖▘▘▖▌▘▄▚▘     ▐▘▖    ▝                ▘         
      ▝▘▖▌ ▗▘▌▘▘▄▀▄▘       ▀▖▘   ▝▄       ▗▝  ▗▝▘           
      ▝▚ ▞▝▝▞▖▀▟▞ ▌ ▘▄▙▘         ▗▝     ▖     ▗             
      ▝▐▐▗▌▚▗▝▞   ▐ ▗▙▘          ▗   ▗      ▖▝              
      ▖▀▐ ▝▄▚▀     ▙▀▞▗    ▐     ▀▞▄▀  ▗  ▖▀                
      ▄▜▝▝▗▐▗      ▌▘▙     ▗▚    ▘▌  ▖▝ ▞▘                  
      ▞▖▐▐▞  ▀▖ ▝ ▖▖▝▀▄    ▗▌   ▐▘▖▗▘▌▚▘                    
      ▜▞▞     ▝ ▖▘▘▝▝▝▞    ▗▘▖   ▗▘ ▄▝                      
      ▝▘      ▝▐ ▝ ▗ ▞ ▚    ▘   ▝▞▙▛                        
                ▚▖▝ ▗ ▚▘    ▘     ▛▌                        
                 ▐▚▝ ▖▗▀    ▞▗▗ ▄▞ ▚                        
                  ▘▚ ▘ ▞     ▖▘▞   ▝▖                       
                   ▀▐▐▚      ▄▄▄▚   ▘▖                      
                   ▗ ▜▘▘       ▘▘   ▝▝                      
                   ▗ ▝▖        ▗▐▖▀  ▘▘                     
                   ▗▞▖▝  ▝           ▚▗                     
                   ▐▘▝▌▌▘ ▘          ▝ ▖              ▖▗    
                    ▌ ▜▞▘ ▘           ▚              ▘▖▖ ▘  
                    ▜  ▀  ▘                                 
"""

peregrine_falcon = """
                                                            
                                                            
     ▗▗▗▗▝▖▚▗▖▄▗                                            
   ▗▘▖▘▗▖▟▟▞▜▜▛▌▙▄                                          
   ▘▗▞▝▖▞▜▛▙██▀█▘▝█▄                                        
  ▚ ▖▖▄▄█▙█▙█▄▖ ▖▘▖█▜▖                                      
  ▚█▄▄▐▐▖▖ ▝▟▟▝  ▖▗▝▗▞▖▖                                    
   ▘ ▝▙▘▝▚ ▖▜▝ ▝ ▖▗▘▀▗▝▝▗                                   
      ▐▝  ▘▝▘  ▝  ▝▖▀▚▜▘▞▝▄                                 
       ▀▗ ▖  ▘▚   ▌▗▚▗▖▝▖▘▖▀▄                               
        ▘▝ ▗ ▖  ▗▚▜▚█▜▐▞▄▚▗▘▄▚▖                             
        ▘▖ ▖  ▝▗▀▘▀▚▐▗▐▀▀▙▌▜▗▖▞▖                            
        ▝▝▝▄ ▘ ▞▘▞▐▗ ▘▞▘▚▗▐▚▞▝▝▐▘                           
         ▘ ▗ ▘▗▛▗▝▝ ▀▝▝▗▚▞▖▘▞▝ ▗▐▐                          
         ▝▝▝   ▖▖▀▞▝▞▖▛▖▘▐ ▀▗▜▞▖▖▗▘▘                        
          ▝ ▗▝ ▙▀▖ ▌▚▝ ▖▜▗▝▞▖▘▞▄▞▗▞▝▐                       
           ▀▝  ▜▗▚▘▖▚▀▖▀▖ ▌▗▗▝▖▚▖▘▄▘▚▚▗                     
           ▝▖▘▚▐▄▘▘▌▝▞▞▝▞▗▗▖▖▀▖▙▜▗▗▝▗▝▖▖                    
            ▚ ▝▖▚▌▜▐▝ ▄▖▌▐ ▀ ▚▞▗▄▚ ▘▚▗ ▞                    
            ▄▝▖▘▝█▘▄▄▀▗▝▞▘▗▖▛▗▝ ▖▝▙▘▘▚▝▗▚                   
             ▚ ▗▘▝▙▖▖▙ ▌▌▙▚▝▝ ▝▝▖▘▖▀▄▄▝▖▞▌                  
              ▘▘▝▖▐█▞▄▖▐ ▌▞▗▝▞▐ ▚▗▝▞▞▖▞▟▗▐                  
              ▚▖▚▀ ▐▙▚▐▞▝▝▄▚▗▗▗▗ ▖▚▝ ▝▄▝▜▐▜                 
               ▗▖▗▝ ▜▜▀█▚▙▀▗▘▚ ▗▚▘▗ ▀▘▚▜▝▝▖▌                
                ▄ ▝▖▞█▛▞▟▞█▌▌▘▚▘▄▗▘▀▞▝▌▗█▖▝▐▖               
                 ▚▘▖▟ ██▖▀▜▞▞█▌▖▗▗ ▚▝ ▌▘▙▜▞▗▗               
                  ▜▗▄ ▌▐█▛▞▜▞▛▟▟▛██▀█▞▜▛▖▌▐▖▚▖              
                  ▝▄▘▚▜▗█▜▌▙▚▞▞▙▛▟▝▙▐▚▜▖▟▞▚▝▌▌              
                  ▝▛▙▌▚▚▗▀▞▗▜▞▞▞▙▀▙▜▙▜▙▜▄▜▄▘▙▚▌             
                  ▌▜▚▟▄▝▙▘▟█▞█▀▙▚▜▞▙▞▙▟▛▟▞▚▀▖▙▘             
                  ▝▞▚▚▄▜▗▘▀▙▛▄▟▚▜▛█▟▐▙▙▛▙▜▚▀▟▀▚▘            
                   ▝▚▙▛▌▙▘▙▀▚▝▙▛▟▐▞▜▚▞▜▟▜▙▜▛▞▚▌▛▖           
                      ▝▙▘▘▜▝▄▐▝▜▟▙▘▌▞▟▜▙█▙█▟▀▛▀▖▄           
                       ▝▟▐▀▌▞▜▝▞▐▚▛▞▝▄▚▞▙▜▙█▚▞▜▛▟▖          
                        ▝█▌▖▚▖▘▙▀▝▜▄▙▗▚▞▄▘▌▜▜█▙▛▚▗          
                         ▐█▟▞▐▚▖▞█▐▜█▞▖▗▘▛▞▚▛▞▚▜▜▞          
                         ▚▞▛▚▚▖▞▖▞▐▐▛▞█▌▌▖▞▜▝▚▙▖▚▀          
               ▗▟▙▜▗▗▄▗▄▀▗▐▖ ▝▘▞▐▗▄▜▙▚▘▞▙▞▞▘▛▚▞▟▀▛▄         
               ▛▖▀▀▀▜▟▝▗▌▘▙▙▛▙▙▀█▙▖ ▜▞▀▛▖▜▟▖▞▚▀▄▜▞▖▚        
            ▖▗▀▝▞▝▘▀▘  ▐▜▀    ▝▀▘▝█  ▚▌▘▘▚▀█▄▘▐▞▚▌▚▄▄       
          ▗▚▐▘▝▘      ▗▘▙         ▝   ▞▐▞ ▞▐▜█▖▛▚▝▙▌▄       
          ▙▚▀       ▝ ▖▛      ▞▖▚▖▀▄  ▝▘▖▘▝▄▐██▙▌▀▄▜▖▚      
          ▀▝ ▖▖▚▘     ▌▜     ▖ ▝▖▐▐▞█▖ ▝▐▐▚▗▘▞▛█▟▚▝▚▝▌▚     
           ▞ ▘        █▝    ▞ ▛▝▝ ▖▝▄▜▌ ▝▞▀▄▖ ▚▜▜▙▌▌▀▞▝     
          ▐▗          ▝▘  ▖▞▖▘     ▝ ▘▛▖ ▐▚▖▞▜ ▜ ▝██▞▐▚▚    
           ▌▖       ▞▗▖  ▘            ▗▘  ▜▟▐▄ ▌▚ ▝▜█▄▚▚▚   
           ▐ ▗▄▞ ▘▝▀▗▝                 ▀▖ ▗▜▌▙▌▌▌   ▀█▙▞▗   
            ▚▖    ▖ ▖▘       ▗         ▘▚  ▙▙▚▜▝▞▖   ▚▝▞▗▐  
            ▐▝▞ ▝ ▌▘           ▖       ▝▞▖ ▝█▞▌▙▙▄    ▀▄ ▝  
            ▐ ▚▝  ▖▘  ▘▘▄       ▝       ▗ ▖ ▚▜▞█▟▐     ▝    
            ▐ ▖▚▘▝ ▖▗                    ▄  ▝▛▞▌▌▞▖         
            ▚▝▗ ▝▘▘ ▖                     ▖  ▚▙▜▐▖▛         
             ▘   ▘▘▘ ▞   ▀▝ ▖             ▘   ▛▙█▛▛▖        
             ▝     ▘▘ ▝ ▝▚▝▗ ▞▝▖▘ ▚▘▚▘    ▝   ▝▙▙▜ ▖        
              ▚    ▘▗▘▝   ▝▗ ▖▘▖▗▘ ▗▘          ▞▛█▙▜        
                      ▘▝       ▝   ▘           ▝▀▚▐▄        
                      ▝                                     
                                                            
"""

bushtit = """
                                                        ▗▄▄▄
     ▞  ▗                                            ▄▟█▜▜▜▛
      ▝▝                                           ▄██▜▟▙▛▛ 
      ▝ ▘                                        ▄██▛▟▟▛▙▛  
       ▖▝                                      ▄██▞▙▜▟▙▀    
        ▖▘                                   ▄██▚▙▜█▛▘▘     
        ▖▄▚ ▖                              ▄█▜▞▛▙█▀         
    ▄▞▜▀▝▝▖▘▀▚▄     ▗▗▗▄▄▚▙▜▐▐▐▄▗▗▗▗     ▄██▙▛█▀▀           
 ▗▗▜▄▐▗▘▌▌▝▝▝▖▐▜▄▞▚▜▚▜▌▌▌▚▙▚▚▐▗▚▚▚▌▄▚▀▛▛███▙▛▞              
▀▗▐▝▐▀▘▚▞▖▚▀▝▗▚▚█▞▟▟▞▄▐▝▟▀▖▀▜▞▞▖▘▖▖▖▖▛▞█▚█▘▘                
   ▞▝▀  ▌▌▖▌▖▜▐▛▛▛▞▞▞▞▟▜▄▛▌▛▌▞▄▝▞▌▌▘▌▛▛▞▙▘                  
    ▖    ▘▘▚▜▜▙▛▀▗▚▚▙▜▞▗▐▘▛▟▖▚▜▐▐▚▞▛▙▜▜▞▄▄▄▄▖               
     ▘        ▗▝▘▞  ▗█▞▘▜▝▞▐▐▗▚▞▞▙▚▜▐▞▚▜▐▟▀▘                
      ▘▄▗▝  ▘▝     ▗█▖▟▜▐▞▙▄▙▙▙▛▙▙▛▛▛▟▜▘▘                   
        ▘ ▝     ▝  ▜▛█▟▙▛▄▙▙▙▀▛█▟▟▜▜▀                       
         ▘▖ ▖ ▖     ▀▀▜▐▜▞▌▚▝▀▝ ▖▗▝                         
           ▘▗             ▖ ▗  ▖▄▘   ▘                      
             ▝▝▖▄▝ ▖▘    ▘ ▗▗▝▗▝    ▐                       
                 ▝  ▗▄▚▖▙ ▝ ▐▀▘     ▗    ▝                  
                     ▝▜  ▝▄▟▘       ▗ ▝                     
                       ▝▗█▟▝▀       ▝ ▌                     
                        ▝▞▌▖ ▘▗     ▝▖▌                     
                            ▖  ▝ ▗▄   ▌                     
                             ▘▗     ▘▗▐▗                    
                                ▘▘ ▖    ▝▗                  
                                                            
"""

black_heron = """
                                                            
                                                            
                                 ▗▄▗▄                       
                             ▗▟▜█▙▜▙▚▌▜▘▗                   
                           ▗▟██▜▛███▀▀▟▟▄▞▗                 
                          ▗█▜▘     ▝▜█▚▝▀█▙▌                
                         ▞▀▘    ▗   ▚ ▌▘▖ ▌▝▘▄              
                       ▗▝      ▝ ▝▝ ▞▀▀▀▗█▄▛▀ ▘▌▖           
                      ▞   █▀▝ ▘▗ ▖ ▝▗▐▖▄▄▀▀▀██▙▙▟▞▖▖        
                    ▖▘  ▌▘  ▀▗     ▘   ▘▘▖    ▝▀▀▜█▄▌       
                  ▗▘   ▝     ▌           ▖          ▝       
                ▗▝   ▄ ▞ ▀  ▝▖▄          ▖                  
               ▖▘    ▚▝     ▐  ▝  ▘     ▗                   
              ▝      ▘ ▘    ▝  ▘        ▖                   
             ▞     ▄▘  ▝     ▞         ▐                    
            ▞ ▝  ▝▘ ▗      ▖▗▝▝      ▗▚▘                    
           ▞  ▘ ▚▛   ▖  ▗ ▚▗▗▐▞▘▘▘  ▗▗                      
          ▞   ▌▟▝   ▝  ▖▗▚▗▘▙▛▄   ▖▞▗▘                      
         ▝▌▝  ▜        ▝▟▖▚▀▚▛▞▖▖▖▘ ▘                       
       ▗▘▞▗ ▐     ▝   ▗▀▞▌▚█▘   ▝▟▝                         
       ▌▄▘▐  ▌      ▝▖▛▝▟▗█    ▖▞▘                          
      ▗▐▛  ▗▌▘   ▗▗▚▀▘▌▚▙▚▘    ▖▞                           
      ▞█▘▗▗▄▀▗▞▝▞▘▘▄▟▐▞▟▙▌    ▞▘                            
     ▐▐▚▗▗ ▘▐▞▝▝ ▐▐▗▙▜▐  ▝  ▖▛                              
     ▖▙▖▗▞▗▝ ▘▗▗▝▌▛▟▟▚▌▘ ▗▖▘▞                               
     ▚▚ ▖▘ ▖▗▘▌▞▟▟▛▛▝▞▄▟▜▘ ▛                                
     ▞   ▌▄▝▞▄▚▙▛▌▟▐██▝▖█▘▛                                 
    ▝▌▘▝ ▐▗▚▜▞█▐▞▚▀▚▛▖▘▗▘▗▘                                 
     ▜▚▘▀▐▀▛▛▞▝▗▝▖▗▐   ▗ ▄▘                                 
     ▖▖▘▘▄▜▚▞▖▀▗▀▌▗▞   ▐▘▄▘                                 
     ▚▚▀▄▙▘▌▛▙▛▘ ▘ ▖    ▀ ▖                                 
     ▚▘▚▐▐▚▜▛▞   ▚ ▖    ▐ ▝                                 
     ▌▐▘▟▐▟▀     ▖ ▖     ▘▝                                 
     ▝▜▐▝▘       ▐ ▖     ▘ ▘     ▖                          
                 ▗ ▖     ▐ ▝▖▄ ▘                            
                 ▐ ▗ ▗▌▘▝▘ ▜▘   ▗ ▘                         
              ▖ ▗▌ ▀▞▘ ▀▐▀▖  ▜▗▘   ▐▄                       
             ▐▀█▞▙ ▚▀▌▚▗▖▖▀▙▞▌▝▞▖▌▀ ▚                       
           ▗▄▝▀ ▝▝▄▜▚ ▙▐▄▖▞▗▚▝▚▐▗▄▀▖▗   ▖                   
          ▘▘    ▝ ▘▖▌▝▖▗▗▖▝█ ▜▛▖▚▗▚▄█▝                      
                   ▐▌▖▝▝▘▖▄ ▝▘▖▜▘▌▀▀                        
                  ▚ ▝▐▘ ▙▚ ▗▞▛▐▀▄▙                          
                 ▝▖ ▌ ▀ ▞▖▄▀    ▚▛                          
                   ▗ ▚▌▀ ▟▘     ▞▘                          
                   ▘                                        
                                                            
"""

red_tailed_hawk = """
                                                            
                                                 ▗▛  ▗▖     
                                             ▄▘▗▐▀ ▄▜▀      
                                           ▗▞▌▞▞▝▝▞▝ ▗▗▀    
                                          ▞▘▘▝ ▚▝▘▖▖▀ ▖▞▝   
                                        ▖▘ ▝ ▘▘ ▖▝▞▗▝▖▀     
                                     ▗▝▖▞▝▝▝▗▖ ▘▝▗▐ ▘▌      
                                    ▞▖▘▗▝ ▌▝▗▘▗▞▝▄▗▝▞       
                                   ▖ ▗▘    ▖▝▗▗ ▘▖▘▞        
                                 ▗▝▝▝ ▘▐▝▖▚▝▖▞ ▘▘▖▘▌        
                                ▖▚ ▌▌▘ ▘▖▗▗▝▖▗▘▌▞▗▘         
                     ▞▞ ▘▘▚▗  ▗▐▝▖▞ ▗  ▘▞▝▖▚▐▗▘▞▗▚          
                   ▗▚▗▝▗ ▗ ▖▘▘▌▘▖▖▖▘▘▗▝▝▖▚▝▞▖▖▌▞▝           
   ▖▘▖  ▝  ▄▖▖▗▖▖▖▖▖▖▖▝▗▚▗▘▖▝▘▝▗▘▞▗▐▝▖▘▙▝▖▌▞▝▝              
   ▗▘▄▟▚▜▐▀▄▙▚▌▛▞▙▙▚▙▚█▐▐▖▚  ▘▘▖▘▞▖▖▌▞▞▖▌▝▖▘▘               
   ▗ ▄▙▀▞▝▞▗▀▟▝▄▜▗▞▌▞▙▚▚▚▐▘▖▘  ▗▝ ▄▚▞▞▖▌▞▝▝                 
    ▝▚▜▀▌▛▖▖▙▖▘▘▀▘▌▚▚▖▌▝▖▌▌▄▄▗▖  ▝ ▗▝▐▐▝                    
       ▀▝▐▟▝▗▖▀▌▚▝▐▝▖▞▞▚▚▚▌▌▘▚▞▞▖▘▖▘▐▝▗  ▘▖                 
             ▀▝▝▖▛▟▐▗▐▗▚▝▖▚▐█▚▝▖▚▘▞▖▘▝▗▗  ▗ ▖▗▝             
                   ▝▘▘▘▘▚▝▘▝▝▝ ▝▌▄▘▌▚ ▘ ▌▖ ▗▗ ▝▝▘           
                               ▀▜▗▚▝▞▖  ▝▖▗ ▌▝▝▝▘           
                              ▝▗▝▚▌▀▞▗▘▝ ▝ ▖▖▝▘▞            
                              ▘▖▝▖▜▝▝▚▝▞▗▀ ▖ ▘▘▄            
                              ▘▞▐▗▝▛ ▘   ▖ ▝▝▗▘             
                             ▝▖▘▞ ▗▝ ▖▖ ▘▞▝▗▞▘              
                               ▀▝▗▚▐ ▖▘▘▖▖▌▘                
                                    ▝▀ ▀                    
                                                            
                                                            
"""

rock_pigeon = """
                                                            
       ▝▝   ▘                                               
                                                            
    ▝  ▗▖▖       ▖                                          
   ▗ ▖   ▘        ▖                                         
   ▝▞▗▘           ▗                                         
  ▝▝               ▖                                        
       ▖▖           ▗                                       
                  ▖                                         
      ▗ ▝            ▘ ▗                                    
      ▝        ▗    ▘    ▗                                  
                  ▝        ▘▗                               
      ▘   ▗▗    ▝▝ ▖▝         ▘▖                            
             ▗ ▘▘               ▘▖                          
     ▝      ▝                     ▖                         
     ▗               ▝            ▗▘▖                       
      ▖ ▖                ▖ ▗ ▘▗     ▗▗                      
          ▗               ▝     ▘ ▗▗  ▚                     
            ▝ ▖                    ▖  ▝▐▝                   
        ▘      ▖                  ▗  ▗ ▘ ▘▗                 
         ▝ ▝▝                   ▗▝  ▖▘▖  ▝▖                 
           ▘     ▘            ▗▝▗ ▗▗  ▘   ▝ ▝▖              
             ▘  ▖ ▘▞    ▖▖▗ ▘▝  ▖▗  ▗▘ ▝ ▚▗▐ ▝▖▘▖▖          
               ▘     ▖▘▘▗▗ ▗▗ ▝▖▝ ▗ ▖▖▞▗▗▗    ▘▗ ▝▘▄        
                 ▝ ▖  ▝ ▖▖▗ ▗▝   ▄ ▘     ▗▖▞   ▖    ▝▘▗     
                     ▗     ▝ ▝▝▝▗       ▞▗ ▗▗▘ ▗ ▘ ▖▖▗▗▝▖   
                      ▘▖▚         ▝▝ ▝▄▖▖▌▀▖▘▀▀▝ ▘▖▖▖  ▘    
                     ▗▘ ▘ ▘ ▗▐            ▘▝▝  ▞▝▞▝▗ ▖▝▖    
                     ▖▚▘   ▄ ▖                  ▝▗▀▗▖ ▘ ▘   
              ▖▖▖▀▄▚▗▘▌▖▗  ▘▞                      ▘▝▚▚ ▖▗  
          ▝▖▗▝ ▀▘▘▌▌▝▝  ▘▘▘▖▌▖▗  ▗                    ▗ ▀   
                  ▗ ▐▗▖▌▌▜ ▌▘▝▝                      ▗      
                        ▐ ▀                           ▞▗▗   
                                                            
"""

common_raven = """
                                                            
                                            ▗ ▖ ▖▗▗         
                                          ▗ ▘▘ ▖▖ ▖ ▝       
                                     ▗▗ ▘▝▖▖ ▞  ▗ ▗ ▘▌▘     
                                 ▗ ▞  ▘▄▖▚▝▖▘▖▗▝   ▐▚▝▗▖▖   
                                ▝▄▗ ▚▗▀ ▘▘▗▚▀▗▗ ▖▝▗▖ ▌ ▖ ▗  
                            ▗▐▝▞▄▗▗▞ ▘▘▌▖▌▚▚▐▗▗▖▝▖ ▖▘   ▝▖▖ 
                          ▐▗▐▝▞▝▖▖▌▀▚▘▌▝▝▗ ▚▖▌▗▗▘▝        ▘ 
                      ▗▗ ▘ ▗▗▝▖▘▗ ▗▝ ▝ ▘▀▗▘▖▞▝▚▖▝▖▘         
                    ▖▘ ▗▀▝▝ ▌▚▗▗▖▝▗▗▝▗▝▗▝ ▗▝ ▞▗▝▞           
                   ▌  ▖ ▗▗▘▘ ▖   ▌▘▚▗▖  ▖▝ ▗▝ ▝             
                 ▖▘▘▀▝ ▀▚▖▞ ▘ ▘▘▘ ▘▖▘▝▞▝  ▖▘ ▘              
              ▖▝ ▘ ▘▖▖▚▘▘▝▗▗▗▚▐▝▝▗▝ ▘ ▗▘▝▗▗                 
          ▗▗▝▝▗▚▄▄▜▝ ▝▝▖▚▘▘▖▖   ▖ ▝▝▝▝ ▗ ▘                  
       ▗▗▘▌ ▝▀▞▗▗ ▖▝ ▗▘▝    ▘▘▞▗▗▝▗▖▞▝ ▘                    
      ▘▌▘▘▖▞▐▗▗▝▗▝▝ ▘         ▘▚▗▝ ▗                        
    ▗▝▝ ▘▘▄▀▖▝ ▝                 ▖▐▗                        
  ▖ ▘    ▚▄▝ ▘                   ▝▖▖▝▖▖                     
                                   ▝▖▖▗▝▝▝▞▖▘               
                                  ▖▘▞▝▗▗▚▚▗▗                
                                     ▘▖▝▝ ▝                 
                                                            
"""

# Dictionary containing bird information
birds_info = {
    "Northern Cardinal": {
        "Description": "A bright red, seed-eating bird in the cardinal family.", 
        "Habitat": "Woodlands, gardens, shrublands, and swamps.",
        "Depiction": northern_cardinal
        },
    "Nuttall's Woodpecker": {
        "Description": "A small woodpecker native to California.", 
        "Habitat": "Oak woodlands and mixed deciduous forests.",
        "Depiction" : nuttall_woodpecker
        },
    "Rock Pigeon": {
        "Description": "Common city pigeon with a wide range of plumage colors.", 
        "Habitat": "Urban areas, cliffs, and underpasses.",
        "Depiction": rock_pigeon
        },
    "Peregrine Falcon": {
        "Description": "Fastest bird in the world, known for its speed during a hunt.", 
        "Habitat": "Wide range including mountains, coastal cliffs, and skyscrapers.",
        "Depiction": peregrine_falcon
        },
    "Black-crowned Night Heron": {
        "Description": "Medium-sized heron with a black crown and back.", 
        "Habitat": "Freshwater wetlands, estuaries, and marshes.",
        "Depiction": black_heron
        },
    "Western Bluebird": {
        "Description": "Small thrush with a blue top and a reddish breast.", 
        "Habitat": "Open woodlands and farmlands.",
        "Depiction": western_bluebird
        },
    "House Sparrow": {
        "Description": "Small bird, often found in urban environments.", 
        "Habitat": "Urban areas, parks, and gardens.",
        "Depiction": house_sparrow
        },
    "Red-tailed Hawk": {
        "Description": "One of the most common hawks in North America.", 
        "Habitat": "Open country, woodlands, prairies, and mountains.",
        "Depiction": red_tailed_hawk
        },
    "Bushtit": {
        "Description": "Tiny, long-tailed bird of the American bushtit family.", 
        "Habitat": "Forests, thicket, and shrublands.",
        "Depiction": bushtit
        },
    "Common Raven": {
        "Description": "Large all-black bird, famous for its intelligence.", 
        "Habitat": "Varied, from Arctic tundra to deserts and mountains.",
        "Depiction": common_raven
        },
}

@app.route('/bird', methods=['GET'])
def get_bird_info():
    bird_name = request.args.get('name', type=str)
    if bird_name in birds_info:
        return jsonify(birds_info[bird_name])
    else:
        return jsonify({"error": "Bird not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
