import streamlit as st
import pandas as pd
import mysql.connector

# Function to initialize the database connection
def create_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Jesseryder',
        database='defence_management'
    )
    return conn

# Function to execute SQL queries
def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def perform_crud_operation(operation, table):
    conn = create_connection()
    cursor = conn.cursor()  # Initialize cursor outside conditional blocks

    if operation == 'View':
         
        # Implement logic to view data
        
        data = pd.read_sql(f'SELECT * FROM {table}', conn)
        st.dataframe(data)
        
    
    elif operation == 'Add':
     st.write(f"Add {table}")

     if table == "Personnel":
        # For Personnel table, gather user inputs
        personnel_id = st.number_input("Personnel ID:", min_value=1, step=1)
        personnel_name = st.text_input("Personnel Name:")
        personnel_ranking = st.text_input("Personnel Ranking:")
        contact_info = st.text_input("Contact Info:")
        unit_id = st.number_input("Unit ID:", min_value=1, step=1)
        mission_id = st.number_input("Mission ID:", min_value=1, step=1)
        deployment_history = st.text_area("Deployment History:")

        # Button to trigger the add action
        if st.button("Add Personnel"):
            try:
                # Insert data into the Personnel table
                insert_query = f"INSERT INTO Personnel (PersonnelID, PersonnelName, PersonnelRanking, ContactInfo, UnitID, MissionID, DeploymentHistory) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (personnel_id, personnel_name, personnel_ranking, contact_info, unit_id, mission_id, deployment_history))
                conn.commit()
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

     elif table == "Units":
        # For Units table, gather user inputs
        unit_id = st.number_input("Unit ID:", min_value=1, step=1)
        unit_name = st.text_input("Unit Name:")
        location = st.text_input("Location:")
        commanding_officer = st.text_input("Commanding Officer:")
        formation_date = st.date_input("Formation Date:")

        # Insert data into the Units table
        if st.button("Update All"):
            try:
                insert_query = f"INSERT INTO Units (UnitID, UnitName, Location, CommandingOfficer, FormationDate) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (unit_id, unit_name, location, commanding_officer, formation_date))
                conn.commit()
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

     elif table == "Missions":
        # For Missions table, gather user inputs
        mission_id = st.number_input("Mission ID:", min_value=1, step=1)
        title = st.text_input("Title:")
        description = st.text_area("Description:")
        start_date = st.date_input("Start Date:")
        end_date = st.date_input("End Date:")
        location = st.text_input("Location:")
        status = st.text_input("Status:")
        unit_id = st.number_input("Unit ID:", min_value=1, step=1)

        # Insert data into the Missions table
        if st.button("Add Mission"):
            try:
                insert_query = f"INSERT INTO Missions (MissionID, Title, Description, StartDate, EndDate, Location, Status, UnitID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (mission_id, title, description, start_date, end_date, location, status, unit_id))
                conn.commit()
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

    # Similar logic for other tables (Equipment, Logistics, Training Courses)...
     if table == "Equipment":
        # For Equipment table, gather user inputs
        equipment_id = st.number_input("Equipment ID:", min_value=1, step=1)
        equipment_type = st.text_input("Equipment Type:")
        equipment_status = st.text_input("Equipment Status:")
        #personnel_id = st.number_input("Personnel ID:", min_value=1, step=1)
        #unit_id = st.number_input("Unit ID:", min_value=1, step=1)

        # Button to trigger the add action
        if st.button("Add Equipment"):
            try:
                # Insert data into the Equipment table
                insert_query = f"INSERT INTO Equipment (EquipmentID, Type, Status) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (equipment_id, equipment_type, equipment_status))
                conn.commit()
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
     if table == "Logistics":
        # For Logistics table, gather user inputs
        request_id = st.number_input("Request ID:", min_value=1, step=1)
        #personnel_name = st.text_input("Personnel Name:")
        #items_requested = st.text_input("Items Requested:")
        requested_quantity = st.number_input("Requested Quantity:", min_value=1, step=1)
        delivery_date = st.date_input("Delivery Date:")
        personnel_id = st.number_input("Personnel ID:", min_value=1, step=1)
        equipment_id = st.number_input("Equipment ID:", min_value=1, step=1)
        unit_id = st.number_input("Unit ID:", min_value=1, step=1)

        # Button to trigger the add action
        if st.button("Add Logistics"):
            try:
                # Insert data into the Logistics table
                insert_query = f"INSERT INTO Logistics (RequestID,  RequestedQuantity, DeliveryDate, PersonnelID, EquipmentID, UnitID) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (request_id, requested_quantity, delivery_date, personnel_id, equipment_id, unit_id))
                conn.commit()
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
     if table == "Trainingcourses":
        # For Training Courses table, gather user inputs
        course_id = st.number_input("Course ID:", min_value=1, step=1)
        title = st.text_input("Title:")
        description = st.text_area("Description:")
        instructor = st.text_input("Instructor:")
        start_date = st.date_input("Start Date:")
        end_date = st.date_input("End Date:")
        location = st.text_input("Location:")

        # Button to trigger the addition
        if st.button("Add"):
            # Insert data into the Training Courses table
            insert_query = f"INSERT INTO trainingcourses (CourseID, Title, Description, Instructor, StartDate, EndDate, Location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (course_id, title, description, instructor, start_date, end_date, location))
            
            conn.commit()
            st.success("Data added successfully!")
    elif operation == 'Update':
    # Implement logic to update data
     st.write(f"Update {table}")

     if table == "Units":
        # For Units table, gather user input for UnitID
        unit_id_to_update = st.number_input("Enter Unit ID to update:", min_value=1, step=1)

        # Check if the specified UnitID exists in the database
        check_query = f"SELECT * FROM Units WHERE UnitID = {unit_id_to_update}"
        cursor.execute(check_query)
        existing_unit = cursor.fetchone()

        if existing_unit:
            # Display existing details for the specified UnitID
            st.write(f"Existing details for Unit ID {unit_id_to_update}:")
            st.write(existing_unit)

            # Gather new details from the user
            new_unit_name = st.text_input("Enter new Unit Name:", value=existing_unit[1])
            new_location = st.text_input("Enter new Location:", value=existing_unit[2])
            new_commanding_officer = st.text_input("Enter new Commanding Officer:", value=existing_unit[3])
            new_formation_date = st.date_input("Enter new Formation Date:", value=existing_unit[4])

            # Button to trigger the update
            if st.button("Update"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE Units SET UnitName = %s, Location = %s, CommandingOfficer = %s, FormationDate = %s WHERE UnitID = {unit_id_to_update}"
                    cursor.execute(update_query, (new_unit_name, new_location, new_commanding_officer, new_formation_date))
                    conn.commit()
                    st.success(f"Details for Unit ID {unit_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Unit ID {unit_id_to_update} does not exist in the database.")

     if table == "Missions":
        # For Missions table, gather user input for MissionID
        mission_id_to_update = st.number_input("Enter Mission ID to update:", min_value=1, step=1)

        # Check if the specified MissionID exists in the database
        check_query = f"SELECT * FROM Missions WHERE MissionID = {mission_id_to_update}"
        cursor.execute(check_query)
        existing_mission = cursor.fetchone()

        if existing_mission:
            # Display existing details for the specified MissionID
            st.write(f"Existing details for Mission ID {mission_id_to_update}:")
            st.write(existing_mission)

            # Gather new details from the user
            new_title = st.text_input("Enter new Title:", value=existing_mission[1])
            new_description = st.text_area("Enter new Description:", value=existing_mission[2])
            new_start_date = st.date_input("Enter new Start Date:", value=existing_mission[3])
            new_end_date = st.date_input("Enter new End Date:", value=existing_mission[4])
            new_location = st.text_input("Enter new Location:", value=existing_mission[5])
            new_status = st.text_input("Enter new Status:", value=existing_mission[6])
            new_unit_id = st.number_input("Enter new Unit ID:", min_value=1, step=1, value=existing_mission[7])

            # Button to trigger the update
            if st.button("Update"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE Missions SET Title = %s, Description = %s, StartDate = %s, EndDate = %s, Location = %s, Status = %s, UnitID = %s WHERE MissionID = {mission_id_to_update}"
                    cursor.execute(update_query, (new_title, new_description, new_start_date, new_end_date, new_location, new_status, new_unit_id))
                    conn.commit()
                    st.success(f"Details for Mission ID {mission_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Mission ID {mission_id_to_update} does not exist in the database.")
     
    # Similar logic for other tables (Personnel, Units, Equipment, Logistics, Training Courses)...   
     if table == "Personnel":
        # For Personnel table, gather user input for PersonnelID
        personnel_id_to_update = st.number_input("Enter Personnel ID to update:", min_value=1, step=1)

        # Check if the specified PersonnelID exists in the database
        check_query = f"SELECT * FROM Personnel WHERE PersonnelID = {personnel_id_to_update}"
        cursor.execute(check_query)
        existing_personnel = cursor.fetchone()

        if existing_personnel:
            # Display existing details for the specified PersonnelID
            st.write(f"Existing details for Personnel ID {personnel_id_to_update}:")
            st.write(existing_personnel)

            # Gather new details from the user
            new_personnel_name = st.text_input("Enter new Personnel Name:", value=existing_personnel[1])
            new_personnel_ranking = st.text_input("Enter new Personnel Ranking:", value=existing_personnel[2])
            new_contact_info = st.text_input("Enter new Contact Info:", value=existing_personnel[3])
            new_unit_id = st.number_input("Enter new Unit ID:", min_value=1, step=1, value=existing_personnel[4])
            new_mission_id = st.number_input("Enter new Mission ID:", min_value=1, step=1, value=existing_personnel[5])
            new_deployment_history = st.text_area("Enter new Deployment History:", value=existing_personnel[6])

            # Button to trigger the update action
            if st.button("Update Personnel"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE Personnel SET PersonnelName = %s, PersonnelRanking = %s, ContactInfo = %s, UnitID = %s, MissionID = %s, DeploymentHistory = %s WHERE PersonnelID = {personnel_id_to_update}"
                    cursor.execute(update_query, (new_personnel_name, new_personnel_ranking, new_contact_info, new_unit_id, new_mission_id, new_deployment_history))
                    conn.commit()
                    st.success(f"Details for Personnel ID {personnel_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Personnel ID {personnel_id_to_update} does not exist in the database.")

    # Similar logic for other tables (Personnel, Missions, Equipment, Logistics, Training Courses)...
     if table == "Equipment":
        # For Equipment table, gather user input for EquipmentID
        equipment_id_to_update = st.number_input("Enter Equipment ID to update:", min_value=1, step=1)

        # Check if the specified EquipmentID exists in the database
        check_query = f"SELECT * FROM Equipment WHERE EquipmentID = {equipment_id_to_update}"
        cursor.execute(check_query)
        existing_equipment = cursor.fetchone()

        if existing_equipment:
            # Display existing details for the specified EquipmentID
            st.write(f"Existing details for Equipment ID {equipment_id_to_update}:")
            st.write(existing_equipment)

            # Gather new details from the user
            new_equipment_type = st.text_input("Enter new Equipment Type:", value=existing_equipment[1])
            new_equipment_status = st.text_input("Enter new Equipment Status:", value=existing_equipment[2])
            #new_personnel_id = st.number_input("Enter new Personnel ID:", min_value=1, step=1, value=existing_equipment[3])
           # new_unit_id = st.number_input("Enter new Unit ID:", min_value=1, step=1, value=existing_equipment[4])

            # Button to trigger the update action
            if st.button("Update Equipment"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE Equipment SET Type = %s, Status = %s WHERE EquipmentID = {equipment_id_to_update}"
                    cursor.execute(update_query, (new_equipment_type, new_equipment_status))
                    conn.commit()
                    st.success(f"Details for Equipment ID {equipment_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Equipment ID {equipment_id_to_update} does not exist in the database.")
     if table == "Logistics":
        # For Logistics table, gather user input for Request ID
        request_id_to_update = st.number_input("Enter Request ID to update:", min_value=1, step=1)

        # Check if the specified Request ID exists in the database
        check_query = f"SELECT * FROM Logistics WHERE RequestID = {request_id_to_update}"
        cursor.execute(check_query)
        existing_logistics = cursor.fetchone()

        if existing_logistics:
            # Display existing details for the specified Request ID
            st.write(f"Existing details for Request ID {request_id_to_update}:")
            st.write(existing_logistics)

            # Gather new details from the user
            new_personnel_name = st.text_input("Enter new Personnel Name:", value=existing_logistics[1])
            new_items_requested = st.text_input("Enter new Items Requested:", value=existing_logistics[2])
            new_requested_quantity = st.number_input("Enter new Requested Quantity:", value=existing_logistics[3], min_value=1, step=1)
            new_delivery_date = st.date_input("Enter new Delivery Date:", value=existing_logistics[4])
            new_personnel_id = st.number_input("Enter new Personnel ID:", value=existing_logistics[5], min_value=1, step=1)
            new_equipment_id = st.number_input("Enter new Equipment ID:", value=existing_logistics[6], min_value=1, step=1)
            new_unit_id = st.number_input("Enter new Unit ID:", value=existing_logistics[7], min_value=1, step=1)

            # Button to trigger the update action
            if st.button("Update Logistics"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE Logistics SET PersonnelName = %s, ItemsRequested = %s, RequestedQuantity = %s, DeliveryDate = %s, PersonnelID = %s, EquipmentID = %s, UnitID = %s WHERE RequestID = {request_id_to_update}"
                    cursor.execute(update_query, (new_personnel_name, new_items_requested, new_requested_quantity, new_delivery_date, new_personnel_id, new_equipment_id, new_unit_id))
                    conn.commit()
                    st.success(f"Details for Request ID {request_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Request ID {request_id_to_update} does not exist in the database.")
    
     if table == "Trainingcourses":
        # For Training Courses table, gather user input for Course ID
        course_id_to_update = st.number_input("Enter Course ID to update:", min_value=1, step=1)

        # Check if the specified Course ID exists in the database
        check_query = f"SELECT * FROM trainingcourses WHERE CourseID = {course_id_to_update}"
        cursor.execute(check_query)
        existing_course = cursor.fetchone()

        if existing_course:
            # Display existing details for the specified Course ID
            st.write(f"Existing details for Course ID {course_id_to_update}:")
            st.write(existing_course)

            # Gather new details from the user
            new_title = st.text_input("Enter new Title:", value=existing_course[1])
            new_description = st.text_area("Enter new Description:", value=existing_course[2])
            new_instructor = st.text_input("Enter new Instructor:", value=existing_course[3])
            new_start_date = st.date_input("Enter new Start Date:", value=existing_course[4])
            new_end_date = st.date_input("Enter new End Date:", value=existing_course[5])
            new_location = st.text_input("Enter new Location:", value=existing_course[6])

            # Button to trigger the update
            if st.button("Update"):
                try:
                    # Execute the update query
                    update_query = f"UPDATE trainingcourses SET Title = %s, Description = %s, Instructor = %s, StartDate = %s, EndDate = %s, Location = %s WHERE CourseID = {course_id_to_update}"
                    cursor.execute(update_query, (new_title, new_description, new_instructor, new_start_date, new_end_date, new_location))
                    conn.commit()
                    st.success(f"Details for Course ID {course_id_to_update} updated successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error(f"Row with Course ID {course_id_to_update} does not exist in the database.")



    elif operation == 'Delete':
    # Implement logic to delete data
     st.write(f"Delete {table}")

     if table == "Units":
        # For Units table, gather user input for UnitID
        unit_id_to_delete = st.number_input("Enter Unit ID to delete:", min_value=1, step=1)

        # Button to trigger the delete action
        if st.button("Delete Unit"):
            # Check if there are dependent rows in the missions table
            check_missions_query = f"SELECT * FROM missions WHERE UnitID = {unit_id_to_delete}"
            cursor.execute(check_missions_query)
            dependent_rows = cursor.fetchall()

            if dependent_rows:
                st.error(f"Cannot delete Unit ID {unit_id_to_delete} as it is referenced in the missions table.")
            else:
                # Proceed with the deletion in the units table
                delete_query = f"DELETE FROM Units WHERE UnitID = {unit_id_to_delete}"
                cursor.execute(delete_query)
                conn.commit()
                st.success(f"Row with Unit ID {unit_id_to_delete} deleted successfully!")

    # Similar logic for other tables (Personnel, Equipment, Logistics, Training Courses)...
     elif table == "Missions":
        # For Missions table, gather user input for MissionID
        mission_id_to_delete = st.number_input("Enter Mission ID to delete:", min_value=1, step=1)

        # Button to trigger the delete action
        if st.button("Delete Mission"):
            # Check if there are dependent rows in other tables (e.g., logistics) referencing this MissionID
            check_dependent_query = f"SELECT * FROM personnel WHERE MissionID = {mission_id_to_delete}"
            cursor.execute(check_dependent_query)
            dependent_rows = cursor.fetchall()

            if dependent_rows:
                st.error(f"Cannot delete Mission ID {mission_id_to_delete} as it is referenced in other tables.")
            else:
                # Proceed with the deletion in the missions table
                delete_query = f"DELETE FROM Missions WHERE MissionID = {mission_id_to_delete}"
                cursor.execute(delete_query)
                conn.commit()
                st.success(f"Row with Mission ID {mission_id_to_delete} deleted successfully!")
     

     elif table == "Personnel":
        # For Personnel table, gather user input for PersonnelID
        personnel_id_to_delete = st.number_input("Enter Personnel ID to delete:", min_value=1, step=1)

        # Button to trigger the delete action
        if st.button("Delete Personnel"):
            # Check if there are dependent rows in other tables (e.g., logistics) referencing this PersonnelID
            check_dependent_query = f"SELECT * FROM logistics WHERE PersonnelID = {personnel_id_to_delete}"
            cursor.execute(check_dependent_query)
            dependent_rows = cursor.fetchall()

            if dependent_rows:
                st.error(f"Cannot delete Personnel ID {personnel_id_to_delete} as it is referenced in other tables.")
            else:
                # Proceed with the deletion in the personnel table
                delete_query = f"DELETE FROM Personnel WHERE PersonnelID = {personnel_id_to_delete}"
                cursor.execute(delete_query)
                conn.commit()
                st.success(f"Row with Personnel ID {personnel_id_to_delete} deleted successfully!")

    # Similar logic for other tables (Personnel, Units, Equipment, Logistics, Training Courses)...
     if table == "Equipment":
        # For Equipment table, gather user input for EquipmentID
        equipment_id_to_delete = st.number_input("Enter Equipment ID to delete:", min_value=1, step=1)

        # Button to trigger the delete action
        if st.button("Delete Equipment"):
            try:
                # Check if there are dependent rows in other tables (e.g., logistics) referencing this EquipmentID
                check_dependent_query = f"SELECT * FROM logistics WHERE EquipmentID = {equipment_id_to_delete}"
                cursor.execute(check_dependent_query)
                dependent_rows = cursor.fetchall()

                if dependent_rows:
                    st.error(f"Cannot delete Equipment ID {equipment_id_to_delete} as it is referenced in other tables.")
                else:
                    # Proceed with the deletion in the equipment table
                    delete_query = f"DELETE FROM Equipment WHERE EquipmentID = {equipment_id_to_delete}"
                    cursor.execute(delete_query)
                    conn.commit()
                    st.success(f"Row with Equipment ID {equipment_id_to_delete} deleted successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
     if table == "Logistics":
        # For Logistics table, gather user input for Request ID
        request_id_to_delete = st.number_input("Enter Request ID to delete:", min_value=1, step=1)

        # Proceed with the deletion in the Logistics table
        if st.button("Delete"):
            # Proceed with the deletion in the Logistics table
            delete_query = f"DELETE FROM Logistics WHERE RequestID = {request_id_to_delete}"
            cursor.execute(delete_query)
            conn.commit()
            st.success(f"Row with Request ID {request_id_to_delete} deleted successfully!")

    # Similar logic for other tables (Personnel, Units, Missions, Equipment, Training Courses)...
     st.write(f"Delete {table}")

     if table == "Trainingcourses":
        # For Training Courses table, gather user input for Course ID
        course_id_to_delete = st.number_input("Enter Course ID to delete:", min_value=1, step=1)

        # Button to trigger the deletion
        if st.button("Delete"):
            # Proceed with the deletion in the Training Courses table
            delete_query = f"DELETE FROM trainingcourses WHERE CourseID = {course_id_to_delete}"
            cursor.execute(delete_query)
            conn.commit()
            st.success(f"Row with Course ID {course_id_to_delete} deleted successfully!")


            # if dependent_rows:
            #     st.error(f"Cannot delete Course ID {course_id_to_delete} as it is referenced in other tables.")
            # else:
            #     # Proceed with the deletion in the Training Courses table
            #     delete_query = f"DELETE FROM trainingcourses WHERE CourseID = {course_id_to_delete}"
            #     cursor.execute(delete_query)
            #     conn.commit()
            #     st.success(f"Row with Course ID {course_id_to_delete} deleted successfully!")

    
    # Similar logic for other tables (Personnel, Units, Equipment, Logistics, etc.)...
    # Inside the perform_crud_operation function
    elif operation == 'Triggers':
     st.write(f"Triggers for {table}")

     if table == "Units":
        # Add Trigger button for the Units table
        if st.button("Add Trigger for Units"):
            try:
                # Example trigger query without DELIMITER
                trigger_query = """
                CREATE TRIGGER units_before_insert
                BEFORE INSERT ON Units
                FOR EACH ROW
                SET NEW.Location = UPPER(NEW.Location);
                """
                cursor.execute(trigger_query)
                conn.commit()
                st.success("Trigger for Units added successfully!")
            except Exception as e:
                st.error(f"Error adding trigger: {e}")

        # Add button to turn off the trigger
        if st.button("Turn Off Trigger for Units"):
            try:
                # Example query to drop the trigger
                drop_trigger_query = "DROP TRIGGER IF EXISTS units_before_insert;"
                cursor.execute(drop_trigger_query)
                conn.commit()
                st.success("Trigger for Units turned off successfully!")
            except Exception as e:
                st.error(f"Error turning off trigger: {e}")
    # Inside the perform_crud_operation function, add a new conditional block for procedures
    elif operation == 'Procedures':
      st.write(f"Procedures for {table}")
      if table == "Personnel":
        if st.button("Create Procedure for Update Personnel Ranking"):
            st.write("Enter the details for the Update Personnel Ranking procedure:")
            personnel_id = st.number_input("Enter Personnel ID:")
            new_ranking = st.text_input("Enter New Ranking:")
            if st.button("Update Ranking"):
                try:
                    # Example procedure execution query - Replace this with your actual procedure execution query
                    execute_procedure_query = f"CALL update_personnel_ranking({personnel_id}, '{new_ranking}');"
                    cursor.execute(execute_procedure_query)
                    conn.commit()
                    st.success("Procedure update_personnel_ranking executed successfully!")
                except Exception as e:
                    st.error(f"Error executing procedure: {e}")

            # Button to remove the procedure
            if st.button("Remove Procedure for Update Personnel Ranking"):
                try:
                    # Example procedure removal query - Replace this with your actual procedure removal query
                    remove_procedure_query = "DROP PROCEDURE IF EXISTS update_personnel_ranking;"
                    cursor.execute(remove_procedure_query)
                    conn.commit()
                    st.success("Procedure for Update Personnel Ranking removed successfully!")
                except Exception as e:
                    st.error(f"Error removing procedure: {e}")



    elif operation == 'Nested Query':
      st.write(f"Nested Query for {table}")

    # Input field for the nested query
      nested_query_input = st.text_input("Enter Nested Query:")

      if st.button("Run Nested Query"):
        try:
            # Execute the nested query
            cursor.execute(nested_query_input)

            # Fetch and display the result
            result = cursor.fetchall()
            st.write("Result of Nested Query:")
            st.write(result)

            # Commit the changes (if any)
            conn.commit()

            st.success("Nested Query executed successfully!")
        except Exception as e:
            st.error(f"Error executing nested query: {e}")

    elif operation == 'Join Query':
      st.write("Join Query")

    # Provide input fields for tables and join conditions
      table1 = st.text_input("Enter first table name:")
      table2 = st.text_input("Enter second table name:")
      join_condition = st.text_input("Enter join condition (e.g., table1.UnitID = table2.UnitID):")

      if st.button("Run Join Query"):
        try:
            # Build and execute the join query
            join_query = f"SELECT * FROM {table1} JOIN {table2} ON {join_condition};"
            cursor.execute(join_query)
            result = cursor.fetchall()

            # Display the result
            st.write(f"Result of Join Query: {result}")
        except Exception as e:
            st.error(f"Error executing join query: {e}")

    elif operation == 'Aggregate':
      st.write("# Aggregate Query")

    # Add a heading for context
      st.write("This aggregate query gives the total requested quantity of items for each personnel in the logistics table.")

    # Example: Total requested quantity of items for each personnel
      query = """
      SELECT PersonnelID, SUM(RequestedQuantity) AS TotalRequestedQuantity
      FROM logistics
      GROUP BY PersonnelID;
      """

      try:
        cursor.execute(query)
        result = cursor.fetchall()

        # Display the result
        st.table(result)

      except Exception as e:
        st.error(f"Error executing aggregate query: {e}")



# Main function
def main():
    st.title("Defense Management System")

    # Sidebar
    sidebar_option = st.sidebar.selectbox("Select Option:", ["Login", "Dashboard"])

    if sidebar_option == "Login":
        login()
    elif sidebar_option == "Dashboard":
        dashboard()

def login():
    st.header("Login Page")
    with st.form(key='login_form'):
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        submitted = st.form_submit_button("Login")

        if submitted and username == "abc@usarmy" and password == "fatboy":
            st.success("Login successful!")
            st.session_state.logged_in = True
        elif submitted:
            st.error("Invalid username or password!")

def dashboard():
    if not getattr(st.session_state, 'logged_in', False):
        st.warning("You need to log in first.")
        login()
        return

    # Dashboard
    tables = ["Personnel", "Units", "Missions", "Equipment", "Logistics", "Trainingcourses"]
    selected_table = st.sidebar.selectbox("Select Table:", tables)

    operations = ["View", "Add", "Update", "Delete","Triggers","Procedures","Nested Query","Join Query","Aggregate"]
    selected_operation = st.sidebar.selectbox("Select Operation:", operations)

    perform_crud_operation(selected_operation, selected_table)

if __name__ == '__main__':
    main()
