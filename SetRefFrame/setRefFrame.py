import nuke
import nukescripts


def changeFrame():
    toFrameList = ['Tracker4', 'CornerPin2D', 'FrameHold', 'Roto', 'Transform']
   
    selNode = nuke.selectedNodes()

    if len (selNode) <> 1:
        nuke.message('Select something!')

    else:
        selNode = nuke.selectedNode()
        if selNode.Class() in toFrameList:

            for k in selNode.knobs():
    
                if k == 'reference_frame': # Tracker
                    selNode['reference_frame'].setValue(nuke.frame())
                    print ('%s.%s new value: %s' % (selNode.name(), k, (nuke.frame())))
    
                elif k == 'first_frame': #FrameHold
                    selNode['first_frame'].setValue(nuke.frame())
                    print ('%s.%s new value: %s' % (selNode.name(), k, (nuke.frame())))
                #elif k == 'ref_frame': #Custom Transform, Roto, CornerPin
                    #selNode['ref_frame'].setValue(nuke.frame())



#Add a menu and assign a shortcut
toolbar = nuke.menu('Nodes')
cqnTools = toolbar.addMenu('CQNTools', 'Modify.png')
cqnTools.addCommand('Change reference frame', 'setRefFrame.changeFrame()', 'crtl + shift + alt + f', icon='TimeOffset.png')