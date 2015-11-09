/**
 * Created by Seth on 10/11/2015.
 */

function make_available_classes2() {
    var available_class, a, mouseover, mouseout, chevron_holder, chevron, type_container, type_text, text, txt1, txt2, container1;
    for (var j = 0; j < CLASS_HANDLES.length; j++) {
        if (CLASS_HANDLES[j] != null) {
            available_class = document.createElement('available_class');
            a = document.createElement('Class' + String(j));
            a.setAttribute('style', 'height: 45px; padding:4px; border-bottom-left-radius:9px; ' +
                'border-bottom-right-radius:9px; border-top-left-radius:9px; ' +
                'border-top-right-radius:9px; border-width:2px;');
            a.setAttribute('id', 'container' + String(j));
            a.setAttribute('class', 'list-group-item');
            a.setAttribute('data-toggle', 'collapse');
            a.setAttribute('data-parent', '#accordion');
            a.setAttribute('href', '#collapse' + String(j));
            mouseover = "shade('container" + String(j) + "')";
            mouseout = "unshade('container" + String(j) + "')";
            a.setAttribute('onmouseover', mouseover);
            a.setAttribute('onmouseout', mouseout);
            available_class.appendChild(a);

            //Add chevron_holder
            chevron_holder = document.createElement("chevron_holder");
            chevron_holder.setAttribute('class', 'col-xs-1');
            a.appendChild(chevron_holder);

            //Add chevron
            chevron = document.createElement('chevron');
            chevron.setAttribute('class', 'fa fa-chevron-circle-down');
            chevron_holder.appendChild(chevron);


            //Add container
            container = document.createElement("container");
            container.setAttribute('class', 'col-xs-11');
            container.setAttribute('style', 'font-size: 13px;');
            a.appendChild(container);

             //add class name container
            class_name_holder = document.createElement("name_holder_container");
            class_name_holder.setAttribute('class', 'col-xs-4');
            class_name_holder.setAttribute('style', 'font-size: 14px; font-weight: bold; height: 20px;');
            container.appendChild(class_name_holder);

            //add class name
            p1 = document.createElement('class_name_' + String(j));
            txt1 = document.createTextNode(CLASS_HANDLES[j].get_ubclass());
            p1.appendChild(txt1);
            class_name_holder.appendChild(p1);

            //Add type container
            type_container = document.createElement("type_container");
            type_container.setAttribute('class', 'col-xs-8');
            type_container.setAttribute('style', 'font-size: 14px; font-weight: bold; text-align: right');
            container.appendChild(type_container);

            //add type
            type_text = document.createElement('type');
            var str1 = CLASS_HANDLES[j].DAYS;
            str1 = str1.replace(/\s+/g, '');
            text = document.createTextNode(str1+ ': '+CLASS_HANDLES[j].get_type());
            type_text.appendChild(text);
            type_container.appendChild(type_text);

            //Add container
            container1 = document.createElement("container2");
            container1.setAttribute('class', 'col-xs-12');
            container1.setAttribute('style', 'font-size: 11px; text-align: right');
            container.appendChild(container1);

            //add class times
            p2 = document.createElement('class_name_' + String(j));
            txt2 = document.createTextNode(CLASS_HANDLES[j].get_time());

            p2.appendChild(txt2);
            container1.appendChild(p2);


            if (CLASS_HANDLES[j].get_recitation().length != 0) {
                var sub_group = document.createElement('sub_group');
                sub_group.setAttribute('id', 'collapse' + String(j));
                sub_group.setAttribute('class', 'panel-collapse collapse');
                sub_group.setAttribute('style', 'padding: 4px;');
                var k;
                for (k = 0; k < CLASS_HANDLES[j].get_recitation().length; k++) {
                    var sub_heading = document.createElement('sub_heading');
                    var sub_a = document.createElement('availableClass' + String(j));
                    sub_a.setAttribute('id', 'collapser' + String(j) + String(k));
                    sub_a.setAttribute('style', 'height: 40px; padding:4px; border-bottom-left-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:9px; border-top-right-radius:9px');
                    sub_a.setAttribute('class', 'list-group-item');
                    sub_a.setAttribute('onclick', 'Table1.clicked_class(CLASS_HANDLES[' + String(j) + '].RECITATION[' + String(k) + '], CLASS_HANDLES[' + String(j) + '])');
                    sub_a.setAttribute('href', '#');
                    var sub_mouseover = "shade('collapser" + String(j) + String(k) + "')";
                    var sub_mouseout = "unshade('collapser" + String(j) + String(k) + "')";
                    sub_a.setAttribute('onmouseover', sub_mouseover);
                    sub_a.setAttribute('onmouseout', sub_mouseout);
                    sub_heading.appendChild(sub_a);

                    //Add spin wheel container
                    var plus_square_holder = document.createElement("plus_square_holder");
                    plus_square_holder.setAttribute('class', 'col-xs-1 col-xs-offset-1');
                    sub_a.appendChild(plus_square_holder);

                    //Add plus-square
                    var plus_square = document.createElement('plus_square');
                    plus_square.setAttribute('class', 'fa fa-chevron-circle-right');
                    plus_square_holder.appendChild(plus_square);


                    //Add container
                    var sub_container = document.createElement("container");
                    sub_container.setAttribute('class', 'col-xs-10');
                    sub_container.setAttribute('style', 'font-size: 12px;');
                    sub_a.appendChild(sub_container);

                    //Add type container
                    var sub_type_container = document.createElement("type_container");
                    sub_type_container.setAttribute('class', 'col-xs-10');
                    sub_type_container.setAttribute('style', 'font-size: 13px; font-weight: bold; text-align: right');
                    sub_container.appendChild(sub_type_container);

                    //add type
                    var sub_type_text = document.createElement('type');
                    var sub_text = document.createTextNode(CLASS_HANDLES[j].RECITATION[k].DAYS+ " : " +CLASS_HANDLES[j].RECITATION[k].get_type());
                    sub_type_text.appendChild(sub_text);
                    sub_type_container.appendChild(sub_type_text);

                     //add class name container
                    var sub_class_name_holder = document.createElement("name_holder_container");
                    sub_class_name_holder.setAttribute('class', 'col-xs-11');
                    sub_class_name_holder.setAttribute('style', 'font-size: 11px; text-align: right');
                    sub_container.appendChild(sub_class_name_holder);

                    //add class name
                    var sub_p1 = document.createElement('name_' + String(j));
                    var sub_txt1 = document.createTextNode(CLASS_HANDLES[j].get_recitation()[k].get_time());
                    sub_p1.appendChild(sub_txt1);
                    sub_class_name_holder.appendChild(sub_p1);

                    sub_group.appendChild(sub_heading);
                }
                available_class.appendChild(sub_group);
            }
            //Add parent (with all children to html)
            var list = document.getElementById('accordion-body');
            list.insertBefore(available_class, list.childNodes[0]);
        }
    }
}



/********************************************************************
*               Switch From Wheel to Avilable Courses
*********************************************************************/
function switch_avail_classes(){
    var wheel = document.getElementById("timeout_wheel");
    wheel.style.display = "none";
    make_available_classes2();
}


/********************************************************************
*               Add Classes to "Selected Classes"
*********************************************************************/
function populate_selected_class(class_handle, rec_handle) {
    var p1,p2,txt2, txt1, container, class_name_holder;
    var heading = document.createElement('heading' + class_handle.ID);
    var a = document.createElement('availableClass');
    a.setAttribute('style', 'height: 60px; padding:4px; ' +
        'border-bottom-left-radius:9px; border-bottom-right-radius:9px; ' +
        'border-top-left-radius:9px; border-top-right-radius:9px; vertical-align: middle;' );
    a.setAttribute('id', 'selected_container' + class_handle.ID);
    a.setAttribute('class', 'list-group-item');

    var onmouseover = "shade('selected_container" + class_handle.ID + "')";
    var onmouseout = "unshade('selected_container" + class_handle.ID + "')";
    a.setAttribute('onmouseover', onmouseover);
    a.setAttribute('onmouseout', onmouseout);
    heading.appendChild(a);

    ////Add lock container
    //var lock_icon_holder = document.createElement("lock_icon_holder");
    //lock_icon_holder.setAttribute('class', 'col-md-1');
    //lock_icon_holder.setAttribute('style', 'height: 40px; vertical-align: middle;');
    //a.appendChild(lock_icon_holder);
    //
    ////Add lock
    //var lock_icon = document.createElement('lock_icon');
    //lock_icon.setAttribute('id','lock_icon'+class_handle.ID);
    //lock_icon.setAttribute('class', 'fa fa-unlock');
    //lock_icon.setAttribute('onclick','lock_in_course("lock_icon'+class_handle.ID+'"'+')');
    //lock_icon_holder.appendChild(lock_icon);

    //Add trash container
    var trash_icon_holder = document.createElement("trash_icon_holder");
    trash_icon_holder.setAttribute('class', 'col-md-1');
    trash_icon_holder.setAttribute('style', 'height:50px;');
    a.appendChild(trash_icon_holder);

    //Add trash icon
    var trash_icon = document.createElement('trash_icon');
    trash_icon.setAttribute('id','trash_icon'+class_handle.ID);
    trash_icon.setAttribute('class', 'fa fa-trash-o');
    trash_icon.setAttribute('style', 'vertical-align: middle;');
    trash_icon.setAttribute('onclick','trash_course("trash_icon'+class_handle.ID+'"'+')');
    trash_icon_holder.appendChild(trash_icon);


    //Add container
    container = document.createElement("container");
    container.setAttribute('class', 'col-xs-10');
    container.setAttribute('style', 'font-size: 13px;  text-align:right;');
    a.appendChild(container);

     //add class name container
    class_name_holder = document.createElement("class_name_holder");
    class_name_holder.setAttribute('class', 'col-xs-12');
    class_name_holder.setAttribute('style', 'font-size: 14px; font-weight: bold; height: 20px;');
    container.appendChild(class_name_holder);

    //add class name
    p1 = document.createElement('class_name');
    txt1 = document.createTextNode(class_handle.UBCLASS);// + ' : ' + class_handle.get_days());
    p1.appendChild(txt1);
    class_name_holder.appendChild(p1);

    //Add container
    var class_days_holder = document.createElement("class_days_holder"+class_handle.ID);
    class_days_holder.setAttribute('class', 'col-xs-12');
    class_days_holder.setAttribute('style', 'font-size: 11px; text-align:right;');
    container.appendChild(class_days_holder);

    //add class name
    p1 = document.createElement('class_days');
    txt1 = document.createTextNode(class_handle.DAYS);// + ' : ' + class_handle.get_days());
    p1.appendChild(txt1);
    class_days_holder.appendChild(p1);

    //Add container
    class_time_holder = document.createElement("class_time_holder"+class_handle.ID);
    class_time_holder.setAttribute('class', 'col-xs-12');
    class_time_holder.setAttribute('style', 'font-size: 11px;');
    container.appendChild(class_time_holder);

    //add class times
    p2 = document.createElement('class_time'+class_handle.ID);
    txt2 = document.createTextNode(class_handle.TIME);
    p2.appendChild(txt2);
    class_time_holder.appendChild(p2);

    validate_selected_class(class_handle,rec_handle, heading);
}


/********************************************************************
*               Validate "Selected Classes"
*********************************************************************/
function validate_selected_class(class_handle,rec_handle, heading) {
    var parent,list,node;
    // Case 1: Node is found
    if(SEL_LL.find_node(class_handle,rec_handle)) {
        SEL_LL.remove_node(class_handle,rec_handle);
        parent = document.getElementById('selected_container' + class_handle.ID).remove();
        Table1.clear_cells(class_handle);
        Table1.clear_cells(rec_handle);
    }
    // Case 2: Class is found, so switch its Recitation
    else if (SEL_LL.find_node_by_class(class_handle)) {
        if(!Table1.time_conflict(rec_handle)) {
            node = SEL_LL.return_node_by_id(class_handle);
            Table1.clear_cells(node.rec_handle);
            SEL_LL.switch_node_rec_handle(class_handle, rec_handle);
            Table1.paint_cells(rec_handle);
        }
        else{
            alert("Time Conflict with Recitation");
        }
    }
    // Case 3: Class exists but is a different time slot
    else if(SEL_LL.find_node_by_ubclass(class_handle)){
        if((!Table1.time_conflict(class_handle))&&(!Table1.time_conflict(rec_handle))){
            //remove the node, but get its reference
            node = SEL_LL.return_node_by_ubclass(class_handle);
            parent = document.getElementById('selected_container' + node.class_handle.ID).remove();
            Table1.clear_cells(node.class_handle);
            Table1.clear_cells(node.rec_handle);
            SEL_LL.remove_node_by_class(node.class_handle);
            //add the new node
            SEL_LL.add_node(class_handle, rec_handle);
            list = document.getElementById('selected_class_container');
            list.insertBefore(heading, list.childNodes[0]);
            Table1.paint_cells(class_handle);
            Table1.paint_cells(rec_handle);
        }
        else{
            alert("Time conflict switching the class");
        }

    }
    //No class found, add class and recitation
    else{
        if((!Table1.time_conflict(class_handle))&&(!Table1.time_conflict(rec_handle))) {
            Table1.paint_cells(class_handle);
            Table1.paint_cells(rec_handle);
            SEL_LL.add_node(class_handle, rec_handle);
            list = document.getElementById('selected_class_container');
            list.insertBefore(heading, list.childNodes[0]);
        }
        else{
            alert("Time Conflict");
        }

    }

}



/********************************************************************
*               Lock In "Selected Classes"
*********************************************************************/
function lock_in_course(id){
    var elem = document.getElementById(id);
    var index = id.split('n');
    var text = document.getElementById('selected_container' + index[1]);
    if(elem.getAttribute('class') == 'fa fa-unlock') {
        elem.setAttribute('class', 'fa fa-lock');
        text.removeAttribute('onmouseout');
        text.removeAttribute('onmouseover');
        text.style.backgroundColor = "Gray";
    }
    else{
        elem.setAttribute('class','fa fa-unlock');
        var onmouseover = "shade('selected_container" + index[1] + "')";
        var onmouseout = "unshade('selected_container" + index[1] + "')";
        text.setAttribute('onmouseover', onmouseover);
        text.setAttribute('onmouseout', onmouseout);
        text.style.backgroundColor = "White";
    }
}


/********************************************************************
*         WEEKLY SCHEDULE - Click Trash Icon to Remove Course
*********************************************************************/
function trash_course(id){
    var elem = document.getElementById(id);
    var index = id.split('n');
    var class_id = parseInt(index[1]);

    /* Remove the node from SEL_LL */
    var fake_class_handle = new UbClass(class_id,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ');
    var node = SEL_LL.return_node_by_id(fake_class_handle);
    SEL_LL.remove_node_by_class(fake_class_handle);

    /* Remove the cells from Table */
    Table1.clear_cells(node.class_handle);
    Table1.clear_cells(node.rec_handle);

    /* Remove the container from selected courses */
    var text = document.getElementById('selected_container' + index[1]);
    var removed = text.remove();
}



/********************************************************************
*               Convert Database Times to Table Times
*********************************************************************
*       - Convert from
*                XX:XX AM - XX:XX PM  to
*                XX:XXAM and XX:XXPM
*       - Return array of start and end times for each day
*-------------------------------------------------------------------*/
function convertTimes(db_days,db_time){
    times = [];
    for(var num=0;num<10;num++){
        times[num] = " ";
    }
    /* Check non-time entries */
    if((db_time == 'TBA')||(db_time == 'ARR')){
        return times;
    }
    /* Split Time to round */
    var split_time = db_time.split(" ");
    var round = split_time[3].split(":");
    if((round[1] == '10')||(round[1] == '20')){
        round[1] = '00';
    }
    /* Round */
    if((round[1] == '40')||(round[1] == '50')){
        round[1] = '00';
        if(round[0] == '1'){round[0]="2";}
        else if(round[0] == '2'){round[0]="3";}
        else if(round[0] == '3'){round[0]="4";}
        else if(round[0] == '4'){round[0]="5";}
        else if(round[0] == '5'){round[0]="6";}
        else if(round[0] == '6'){round[0]="7";}
        else if(round[0] == '7'){round[0]="8";}
        else if(round[0] == '8'){round[0]="9";}
        else if(round[0] == '9'){round[0]="10";}
        else if(round[0] == '10'){round[0]="11";}
        else if(round[0] == '11')
        {
            round[0]="12";
            if(split_time[4] == "AM"){
                split_time[4] = "PM";
            }
            else{
                split_time[4] = "AM";
            }
        }
        else if(round[0] == '12'){round[0]='1';}
    }

    split_time[3] = round[0]+":"+round[1];
    var start_time = split_time[0]+split_time[1];
    var end_time = split_time[3]+split_time[4];

    /* Analyze and enter times in the correct day slot */
    if(db_days.indexOf('M') != -1){
        times[0] = "M" + start_time;
        times[1] = "M" + end_time;
    }
    if(db_days.indexOf('T') != -1){
        times[2] = "T" + start_time;
        times[3] = "T" + end_time;
    }
    if(db_days.indexOf('W') != -1){
        times[4] = "W" + start_time;
        times[5] = "W" + end_time;
    }
    if(db_days.indexOf('R') != -1){
        times[6] = "R" + start_time;
        times[7] = "R" + end_time;
    }
    if(db_days.indexOf('F') != -1){
        times[8] = "F" + start_time;
        times[9] = "F" + end_time;
    }
    /* Saturdays not implemented yet */
    //if(db_days.indexOf('S') != -1){
    //    times[10] = "S" + start_time;
    //    times[11] = "S" + end_time;
    //}
    return times;
}

function shade(id){
    var elem = document.getElementById(id);
    elem.style.backgroundColor = "#cce0ff";
}

function unshade(id){
    var elem = document.getElementById(id);
    elem.style.backgroundColor = "white";
}




/********************************************************************
*           FLOWSHEET - Create a Single Block and Add to Container
*********************************************************************/
function create_new_course_block(sem_index, num){
    var course = document.createElement('semester'+String(sem_index));
    var a = document.createElement('course');
    a.setAttribute('style', 'min-height: 90px; min-width: 95px; padding: 10px 2px; ' +
            'border-top-left-radius: 8px;border-top-right-radius: 8px;' +
            'border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;' +
            'border-color: #334455; word-wrap: break-word;' );

    /* Add Blue checkmark if taken, otherwise add a gray hidden mark */
    var image = document.createElement('img');
    image.setAttribute('id',String(DEGREE_HANDLES[num].get_ubclass())+'_check');
    if(DEGREE_HANDLES[num].get_taken() == 1) {
        image.setAttribute('src', 'static/blue_check.png');
        image.setAttribute('style', 'position:absolute; top:0px; left:0px;');
    }
    else{
        image.setAttribute('src', 'static/grayscale_check.png');
        image.setAttribute('style', 'position:absolute; top:0px; left:0px; display:none;');

    }
    a.appendChild(image);

    a.setAttribute('id',String(DEGREE_HANDLES[num].get_ubclass()));
    a.setAttribute('class', 'list-group-item');
    var check_string = "switch_check_type('"+String(DEGREE_HANDLES[num].get_ubclass())+"')";
    a.setAttribute('onclick',check_string);


    //Set Change Color on Hover
    var mouseover = "show_info('"+String(DEGREE_HANDLES[num].get_ubclass())+"',"+String(0)+")";
    var mouseout = "hide_info('"+String(DEGREE_HANDLES[num].get_ubclass())+"',"+String(0)+")";
    a.setAttribute('onmouseover', mouseover);
    a.setAttribute('onmouseout', mouseout);

    //Add pre-req & co-req
    a.setAttribute('pre_req1',DEGREE_HANDLES[num].PRE_REQ1);
    a.setAttribute('pre_req2',DEGREE_HANDLES[num].PRE_REQ2);
    a.setAttribute('pre_req3',DEGREE_HANDLES[num].PRE_REQ3);
    a.setAttribute('co_req1',DEGREE_HANDLES[num].CO_REQ1);
    a.setAttribute('co_req2',DEGREE_HANDLES[num].CO_REQ2);
    course.appendChild(a);


    //course and cap box
    var course_box = document.createElement("course_box");
    course_box.setAttribute('class', 'col-xs-12');
    course_box.setAttribute('style', 'padding:3px;');
    a.appendChild(course_box);

    var span = document.createElement("span");
    span.setAttribute('style', 'height:15px');
    span.setAttribute('class', 'col-xs-12');
    course_box.appendChild(span);

    //Add course name container
    var course_container = document.createElement("course_container");
    course_container.setAttribute('class', 'col-xs-12');
    course_container.setAttribute('style','font-family: Arial Rounded MT Bold, ' +
        'Helvetica Rounded, Arial, sans-serif; font-style: normal; line-height:' +
        ' 23px; font-weight: bold; font-size: 17px;');
    course_box.appendChild(course_container);

    //add course name and link to course description
    var course_name = document.createElement('course_text' + String(num));
    //var course_name = document.createElement('a');
    var course_string = String(DEGREE_HANDLES[num].get_ubclass());
    var URL = 'http://undergrad-catalog.buffalo.edu/coursedescriptions/index.php?frm_abbr=' + course_string.slice(0, (course_string.length - 3)) + '&frm_num=' + course_string.slice(-3);
    if ( (course_string.indexOf("XX") == -1) && (course_string.indexOf("Gen Ed") == -1) ) {
        course_name.setAttribute('style', 'color: blue; text-decoration: underline');
    }
    course_name.onmouseover = function() {
        if ( (course_string.indexOf("XX") == -1) && (course_string.indexOf("Gen Ed") == -1) && (EDITABLE == 0) ) {
            document.body.style.cursor = 'pointer';
        }
    };
    course_name.onmouseout = function() {
        if ( (course_string.indexOf("XX") == -1) && (course_string.indexOf("Gen Ed") == -1) && (EDITABLE == 0) ) {
            document.body.style.cursor = 'auto';
        }
    };
    course_name.onclick = function() {
        if ( (course_string.indexOf("XX") == -1) && (course_string.indexOf("Gen Ed") == -1) && (EDITABLE == 0) ) {
            course_name.setAttribute('style', 'color: #4B0082; text-decoration: underline');
            window.open(URL, '_blank');
            return false;
        }
    };
    var course_name_text = document.createTextNode(DEGREE_HANDLES[num].get_ubclass());
    course_name.appendChild(course_name_text);
    course_container.appendChild(course_name);

    //course title
    var course_title_container = document.createElement("course_title_box");
    course_title_container.setAttribute('class', 'col-xs-12');
    course_title_container.setAttribute('style', 'font-size:11px;font-style:italic;');
    course_title_container.setAttribute('font-family', 'Agency fb');
    a.appendChild(course_title_container);

    //add course name
    var course_title1 = document.createElement('course_title');
    var course_text_title = document.createTextNode(DEGREE_HANDLES[num].get_title());
    course_title1.appendChild(course_text_title);
    course_title_container.appendChild(course_title1);

    var list = document.getElementById('sem'+String(sem_index));
    list.insertBefore(course, list.childNodes[0]);
}

/********************************************************************
*        FLOWSHEET - Checkes for repeats in DEGREE_HANDLES
*********************************************************************/
function search_degree_for_repeats(id){
    for(var p=0;p<DEGREE_HANDLES.length;p++){
        if( id == DEGREE_HANDLES[p].get_ubclass()){
            return true;
        }
    }
    return false;
}


/********************************************************************
*        FLOWSHEET - Show Untaken classes with gray checkmark
*********************************************************************/
function switch_check_visibility(id){
    id = id + '_check';
    var elem = document.getElementById(id);
    if(EDITABLE == 1) {
        if (elem.style.display == "none") {
            elem.style.display = "block";
        }
        else {
            elem.style.display = "none";
        }
    }
}


/********************************************************************
*        FLOWSHEET - Changes checkmark displayed & Indicates as taken
*********************************************************************/
/*  */
function switch_check_type(id){
    var i, course;
    var image_id = id + '_check';
    var elem = document.getElementById(image_id);
    if(EDITABLE == 1) {
        for(i=0;i<DEGREE_HANDLES.length;i++){
            if(id == DEGREE_HANDLES[i].get_ubclass()) {
                if(elem.getAttribute('src') == 'static/blue_check.png') {
                    elem.setAttribute('src', 'static/grayscale_check.png');
                    DEGREE_HANDLES[i].set_not_taken();
                    NUM_USER_CLASSES_APPLIED -= 1;
                    course = DEGREE_HANDLES[i].get_id();

                    data = {'user': USER_ID,
                            'course':course,
                            'update_type':'remove',
                            'num_taken': NUM_USER_CLASSES_APPLIED};
                    console.log(data);
                    $.ajax({
                        type : "POST",
                        url : '/updatedegree',
                        data: JSON.stringify(data, null, '\t'),
                        contentType: 'application/json;charset=UTF-8',
                        success: function(dat) {
                            console.log(dat);
                        }
                    });
                }
                else{
                    elem.setAttribute('src', 'static/blue_check.png');
                    DEGREE_HANDLES[i].set_as_taken();
                    NUM_USER_CLASSES_APPLIED += 1;
                    course = DEGREE_HANDLES[i].get_id();

                    data = {'user': USER_ID,
                            'course':course,
                            'update_type':'add',
                            'num_taken': NUM_USER_CLASSES_APPLIED};
                    console.log(data);
                    $.ajax({
                        type : "POST",
                        url : '/updatedegree',
                        data: JSON.stringify(data, null, '\t'),
                        contentType: 'application/json;charset=UTF-8',
                        success: function(dat) {
                            console.log(dat);
                        }
                    });
                }
                break;
            }
        }
    }
}


/********************************************************************
*        FLOWSHEET - Color Dependencies
*********************************************************************/
function show_info(id, iteration){
    var elem;
    var next;
    elem = document.getElementById(id);
    if(iteration == 0){
        elem.style.backgroundColor = "#8FC8FF";
        iteration += 1;
    }
    else if(iteration == 1){
        elem.style.backgroundColor = "#FFD700";
        iteration += 1;
    }
    else if(iteration == 2){
        elem.style.backgroundColor = "#E6C200";
        iteration += 1;
    }
    else if(iteration == 3){
        elem.style.backgroundColor = "#CCAC00";
        iteration += 1;
    }
    else if(iteration == 4){
        elem.style.backgroundColor = "#B39600";
        iteration += 1;
    }
    else if(iteration == 5){
        elem.style.backgroundColor = "#998100";
        iteration += 1;
    }
    else if(iteration == 6){
        elem.style.backgroundColor = "#806C00";
        iteration += 1;
    }
    else if(iteration == 7){
        elem.style.backgroundColor = "#665600";
        iteration += 1;
    }
    if(elem == null){
        return;
    }
    if(elem.getAttribute('pre_req1')){
        if(elem.getAttribute('pre_req1') != 'none') {
            next = elem.getAttribute('pre_req1');
            show_info(next, iteration);
        }
    }
    if(elem.getAttribute('pre_req2')){
        if(elem.getAttribute('pre_req2') != 'none') {
            next = elem.getAttribute('pre_req2');
            show_info(next, iteration);
        }
    }
    if(elem.getAttribute('pre_req3')){
        if(elem.getAttribute('pre_req3') != 'none') {
            next = elem.getAttribute('pre_req3');
            show_info(next, iteration);
        }
    }
}

/********************************************************************
*        FLOWSHEET - Uncolor Dependencies
*********************************************************************/
function hide_info(id,iteration){
    var elem;
    var next;
    elem = document.getElementById(id);
    elem.style.backgroundColor = "White";
    if(elem.getAttribute('pre_req1')){
        if(elem.getAttribute('pre_req1') != 'none') {
            next = elem.getAttribute('pre_req1');
            hide_info(next, iteration);
        }
    }
    if(elem.getAttribute('pre_req2')){
        if(elem.getAttribute('pre_req2') != 'none') {
            next = elem.getAttribute('pre_req2');
            hide_info(next, iteration);
        }
    }
    if(elem.getAttribute('pre_req3')){
        if(elem.getAttribute('pre_req3') != 'none') {
            next = elem.getAttribute('pre_req3');
            hide_info(next, iteration);
        }
    }
}


/********************************************************************
*           FLOWSHEET - Loop and create Blocks in Semesters
*********************************************************************/
function populate_semesters(){
    for(var sem=0;sem<9;sem++){
        for(var i=0;i<DEGREE_HANDLES.length;i++) {
            if (DEGREE_HANDLES[i].get_sem_index() == sem) {
                create_new_course_block(sem, i);
            }
        }
    }
}






/********************************************************************
*               Spinning Wheel to Used during delay
*********************************************************************/
/**
 * Copyright (c) 2011-2014 Felix Gnass
 * Licensed under the MIT license
 * http://spin.js.org/
 *
 * Example:
    var opts = {
      lines: 12             // The number of lines to draw
    , length: 7             // The length of each line
    , width: 5              // The line thickness
    , radius: 10            // The radius of the inner circle
    , scale: 1.0            // Scales overall size of the spinner
    , corners: 1            // Roundness (0..1)
    , color: '#000'         // #rgb or #rrggbb
    , opacity: 1/4          // Opacity of the lines
    , rotate: 0             // Rotation offset
    , direction: 1          // 1: clockwise, -1: counterclockwise
    , speed: 1              // Rounds per second
    , trail: 100            // Afterglow percentage
    , fps: 20               // Frames per second when using setTimeout()
    , zIndex: 2e9           // Use a high z-index by default
    , className: 'spinner'  // CSS class to assign to the element
    , top: '50%'            // center vertically
    , left: '50%'           // center horizontally
    , shadow: false         // Whether to render a shadow
    , hwaccel: false        // Whether to use hardware acceleration (might be buggy)
    , position: 'absolute'  // Element positioning
    }
    var target = document.getElementById('foo')
    var spinner = new Spinner(opts).spin(target)
 */
(function (root, factory) {

  /* CommonJS */
  if (typeof module == 'object' && module.exports) module.exports = factory();

  /* AMD module */
  else if (typeof define == 'function' && define.amd) define(factory);

  /* Browser global */
  else root.Spinner = factory()
}(this, function () {
  "use strict";

  var prefixes = ['webkit', 'Moz', 'ms', 'O'] /* Vendor prefixes */
    , animations = {} /* Animation rules keyed by their name */
    , useCssAnimations /* Whether to use CSS animations or setTimeout */
    , sheet; /* A stylesheet to hold the @keyframe or VML rules. */

  /**
   * Utility function to create elements. If no tag name is given,
   * a DIV is created. Optionally properties can be passed.
   */
  function createEl (tag, prop) {
    var el = document.createElement(tag || 'div')
      , n;

    for (n in prop) el[n] = prop[n]
    return el
  }

  /**
   * Appends children and returns the parent.
   */
  function ins (parent /* child1, child2, ...*/) {
    for (var i = 1, n = arguments.length; i < n; i++) {
      parent.appendChild(arguments[i])
    }

    return parent
  }

  /**
   * Creates an opacity keyframe animation rule and returns its name.
   * Since most mobile Webkits have timing issues with animation-delay,
   * we create separate rules for each line/segment.
   */
  function addAnimation (alpha, trail, i, lines) {
    var name = ['opacity', trail, ~~(alpha * 100), i, lines].join('-')
      , start = 0.01 + i/lines * 100
      , z = Math.max(1 - (1-alpha) / trail * (100-start), alpha)
      , prefix = useCssAnimations.substring(0, useCssAnimations.indexOf('Animation')).toLowerCase()
      , pre = prefix && '-' + prefix + '-' || '';

    if (!animations[name]) {
      sheet.insertRule(
        '@' + pre + 'keyframes ' + name + '{' +
        '0%{opacity:' + z + '}' +
        start + '%{opacity:' + alpha + '}' +
        (start+0.01) + '%{opacity:1}' +
        (start+trail) % 100 + '%{opacity:' + alpha + '}' +
        '100%{opacity:' + z + '}' +
        '}', sheet.cssRules.length);

      animations[name] = 1
    }

    return name
  }

  /**
   * Tries various vendor prefixes and returns the first supported property.
   */
  function vendor (el, prop) {
    var s = el.style
      , pp
      , i;

    prop = prop.charAt(0).toUpperCase() + prop.slice(1);
    if (s[prop] !== undefined) return prop;
    for (i = 0; i < prefixes.length; i++) {
      pp = prefixes[i]+prop;
      if (s[pp] !== undefined) return pp
    }
  }

  /**
   * Sets multiple style properties at once.
   */
  function css (el, prop) {
    for (var n in prop) {
      el.style[vendor(el, n) || n] = prop[n]
    }

    return el
  }

  /**
   * Fills in default values.
   */
  function merge (obj) {
    for (var i = 1; i < arguments.length; i++) {
      var def = arguments[i];
      for (var n in def) {
        if (obj[n] === undefined) obj[n] = def[n]
      }
    }
    return obj
  }

  /**
   * Returns the line color from the given string or array.
   */
  function getColor (color, idx) {
    return typeof color == 'string' ? color : color[idx % color.length]
  }

  // Built-in defaults
  var defaults = {
    lines: 12             // The number of lines to draw
  , length: 7             // The length of each line
  , width: 5              // The line thickness
  , radius: 10            // The radius of the inner circle
  , scale: 1.0            // Scales overall size of the spinner
  , corners: 1            // Roundness (0..1)
  , color: '#000'         // #rgb or #rrggbb
  , opacity: 1/4          // Opacity of the lines
  , rotate: 0             // Rotation offset
  , direction: 1          // 1: clockwise, -1: counterclockwise
  , speed: 1              // Rounds per second
  , trail: 100            // Afterglow percentage
  , fps: 20               // Frames per second when using setTimeout()
  , zIndex: 2e9           // Use a high z-index by default
  , className: 'spinner'  // CSS class to assign to the element
  , top: '50%'            // center vertically
  , left: '50%'           // center horizontally
  , shadow: false         // Whether to render a shadow
  , hwaccel: false        // Whether to use hardware acceleration (might be buggy)
  , position: 'absolute'  // Element positioning
  };

  /** The constructor */
  function Spinner (o) {
    this.opts = merge(o || {}, Spinner.defaults, defaults)
  }
  // Global defaults that override the built-ins:
  Spinner.defaults = {};
  merge(Spinner.prototype, {
    /**
     * Adds the spinner to the given target element. If this instance is already
     * spinning, it is automatically removed from its previous target b calling
     * stop() internally.
     */
    spin: function (target) {
      this.stop();

      var self = this
        , o = self.opts
        , el = self.el = createEl(null, {className: o.className});

      css(el, {
        position: o.position
      , width: 0
      , zIndex: o.zIndex
      , left: o.left
      , top: o.top
      });

      if (target) {
        target.insertBefore(el, target.firstChild || null)
      }

      el.setAttribute('role', 'progressbar');
      self.lines(el, self.opts);

      if (!useCssAnimations) {
        // No CSS animation support, use setTimeout() instead
        var i = 0
          , start = (o.lines - 1) * (1 - o.direction) / 2
          , alpha
          , fps = o.fps
          , f = fps / o.speed
          , ostep = (1 - o.opacity) / (f * o.trail / 100)
          , astep = f / o.lines

        ;(function anim () {
          i++
          for (var j = 0; j < o.lines; j++) {
            alpha = Math.max(1 - (i + (o.lines - j) * astep) % f * ostep, o.opacity);

            self.opacity(el, j * o.direction + start, alpha, o)
          }
          self.timeout = self.el && setTimeout(anim, ~~(1000 / fps))
        })()
      }
      return self
    }

    /**
     * Stops and removes the Spinner.
     */
  , stop: function () {
      var el = this.el;
      if (el) {
        clearTimeout(this.timeout);
        if (el.parentNode) el.parentNode.removeChild(el);
        this.el = undefined
      }
      return this
    }

    /**
     * Internal method that draws the individual lines. Will be overwritten
     * in VML fallback mode below.
     */
  , lines: function (el, o) {
      var i = 0
        , start = (o.lines - 1) * (1 - o.direction) / 2
        , seg

      function fill (color, shadow) {
        return css(createEl(), {
          position: 'absolute'
        , width: o.scale * (o.length + o.width) + 'px'
        , height: o.scale * o.width + 'px'
        , background: color
        , boxShadow: shadow
        , transformOrigin: 'left'
        , transform: 'rotate(' + ~~(360/o.lines*i + o.rotate) + 'deg) translate(' + o.scale*o.radius + 'px' + ',0)'
        , borderRadius: (o.corners * o.scale * o.width >> 1) + 'px'
        })
      }

      for (; i < o.lines; i++) {
        seg = css(createEl(), {
          position: 'absolute'
        , top: 1 + ~(o.scale * o.width / 2) + 'px'
        , transform: o.hwaccel ? 'translate3d(0,0,0)' : ''
        , opacity: o.opacity
        , animation: useCssAnimations && addAnimation(o.opacity, o.trail, start + i * o.direction, o.lines) + ' ' + 1 / o.speed + 's linear infinite'
        });

        if (o.shadow) ins(seg, css(fill('#000', '0 0 4px #000'), {top: '2px'}));
        ins(el, ins(seg, fill(getColor(o.color, i), '0 0 1px rgba(0,0,0,.1)')))
      }
      return el
    }

    /**
     * Internal method that adjusts the opacity of a single line.
     * Will be overwritten in VML fallback mode below.
     */
  , opacity: function (el, i, val) {
      if (i < el.childNodes.length) el.childNodes[i].style.opacity = val
    }

  });

  function initVML () {

    /* Utility function to create a VML tag */
    function vml (tag, attr) {
      return createEl('<' + tag + ' xmlns="urn:schemas-microsoft.com:vml" class="spin-vml">', attr)
    }

    // No CSS transforms but VML support, add a CSS rule for VML elements:
    sheet.addRule('.spin-vml', 'behavior:url(#default#VML)');

    Spinner.prototype.lines = function (el, o) {
      var r = o.scale * (o.length + o.width)
        , s = o.scale * 2 * r;

      function grp () {
        return css(
          vml('group', {
            coordsize: s + ' ' + s
          , coordorigin: -r + ' ' + -r
          })
        , { width: s, height: s }
        )
      }

      var margin = -(o.width + o.length) * o.scale * 2 + 'px'
        , g = css(grp(), {position: 'absolute', top: margin, left: margin})
        , i

      function seg (i, dx, filter) {
        ins(
          g
        , ins(
            css(grp(), {rotation: 360 / o.lines * i + 'deg', left: ~~dx})
          , ins(
              css(
                vml('roundrect', {arcsize: o.corners})
              , { width: r
                , height: o.scale * o.width
                , left: o.scale * o.radius
                , top: -o.scale * o.width >> 1
                , filter: filter
                }
              )
            , vml('fill', {color: getColor(o.color, i), opacity: o.opacity})
            , vml('stroke', {opacity: 0}) // transparent stroke to fix color bleeding upon opacity change
            )
          )
        )
      }

      if (o.shadow)
        for (i = 1; i <= o.lines; i++) {
          seg(i, -2, 'progid:DXImageTransform.Microsoft.Blur(pixelradius=2,makeshadow=1,shadowopacity=.3)')
        }

      for (i = 1; i <= o.lines; i++) seg(i)
      return ins(el, g)
    };

    Spinner.prototype.opacity = function (el, i, val, o) {
      var c = el.firstChild;
      o = o.shadow && o.lines || 0;
      if (c && i + o < c.childNodes.length) {
        c = c.childNodes[i + o]; c = c && c.firstChild; c = c && c.firstChild
        if (c) c.opacity = val
      }
    }
  }

  if (typeof document !== 'undefined') {
    sheet = (function () {
      var el = createEl('style', {type : 'text/css'});
      ins(document.getElementsByTagName('head')[0], el);
      return el.sheet || el.styleSheet
    }());

    var probe = css(createEl('group'), {behavior: 'url(#default#VML)'});

    if (!vendor(probe, 'transform') && probe.adj) initVML();
    else useCssAnimations = vendor(probe, 'animation')
  }

  return Spinner
}));