#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  Jun 10, 2019 04:34:22 PM +0300  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#d8c7a0} 
    wm focusmodel $top passive
    wm geometry $top 1200x1000+190+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "VRI - Designer"
    vTcl:DefineAlias "$top" "designer" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground {#000000} -tearoff 0 
    canvas $top.can44 \
        -background {#ffffff} -borderwidth 2 -closeenough 1.0 -height 75 \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 125 
    vTcl:DefineAlias "$top.can44" "canvas" vTcl:WidgetProc "designer" 1
    button $top.but47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Save 
    vTcl:DefineAlias "$top.but47" "save_b" vTcl:WidgetProc "designer" 1
    bind $top.but47 <Button-1> {
        lambda e: xxx(e)
    }
    button $top.but48 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Exit 
    vTcl:DefineAlias "$top.but48" "exit_b" vTcl:WidgetProc "designer" 1
    bind $top.but48 <Button-1> {
        lambda e: xxx(e)
    }
    button $top.but50 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Wall 
    vTcl:DefineAlias "$top.but50" "wall_b" vTcl:WidgetProc "designer" 1
    bind $top.but50 <Button-1> {
        lambda e: xxx(e)
    }
    button $top.but51 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Robot 
    vTcl:DefineAlias "$top.but51" "robot_b" vTcl:WidgetProc "designer" 1
    bind $top.but51 <Button-1> {
        lambda e: xxx(e)
    }
    button $top.but52 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Sensor 
    vTcl:DefineAlias "$top.but52" "sensor_b" vTcl:WidgetProc "designer" 1
    bind $top.but52 <Button-1> {
        lambda e: xxx(e)
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can44 \
        -in $top -x 0 -y 0 -width 1000 -relwidth 0 -height 1000 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 1000 -y 840 -width 197 -relwidth 0 -height 54 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 1000 -y 910 -width 197 -height 54 -anchor nw \
        -bordermode ignore 
    place $top.but50 \
        -in $top -x 1000 -y 50 -width 197 -height 54 -anchor nw \
        -bordermode ignore 
    place $top.but51 \
        -in $top -x 1000 -y 130 -width 197 -height 54 -anchor nw \
        -bordermode ignore 
    place $top.but52 \
        -in $top -x 1000 -y 210 -width 197 -height 54 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

