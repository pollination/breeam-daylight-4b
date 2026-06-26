# BREEAM Daylight Assessment

### Recipe Requirements

To successfully run the BREEAM daylight compliance recipe, you must ensure that your Honeybee rooms have a **Honeybee Energy program** assigned to them. 

Because BREEAM maps distinct daylight targets depending on the specific function of a room, the component relies on these programs to split and evaluate your simulation model accurately. 

#### Requirements:
* **Rooms:** Your simulation model must consist of properly defined Honeybee Rooms rather than loose geometry or independent sensor grids.
* **Programs:** Every Honeybee Room must have a Honeybee Energy program assigned to it. If a room has no program assigned, it will auto-assign a default one, `BREEAM::Office_buildings::Occupied_spaces`, during the post-processing phase.

> **NOTE:** The simulation only uses the program to *categorize* the room type. It does not use any underlying schedules, loads, etc. Therefore, **only the program name itself is important**.

#### List of Valid Program Names
Your programs must match one of the following exact text strings:

* `BREEAM::Education_buildings::Preschools`
* `BREEAM::Education_buildings::Higher_education`
* `BREEAM::Healthcare_buildings::Staff_and_public_areas`
* `BREEAM::Healthcare_buildings::Patients_areas_and_consulting_rooms`
* `BREEAM::Multi_residential_buildings::Kitchen`
* `BREEAM::Multi_residential_buildings::Living_rooms_dining_rooms_studies`
* `BREEAM::Multi_residential_buildings::Non_residential_or_communal_spaces`
* `BREEAM::Retail_buildings::Sales_areas`
* `BREEAM::Retail_buildings::Other_occupied_areas`
* `BREEAM::Prison_buildings::Cells_and_custody_cells`
* `BREEAM::Prison_buildings::Internal_association_or_atrium`
* `BREEAM::Prison_buildings::Patient_care_spaces`
* `BREEAM::Prison_buildings::Teaching_lecture_and_seminar_spaces`
* `BREEAM::Office_buildings::Occupied_spaces`
* `BREEAM::Creche_buildings::Occupied_spaces`
* `BREEAM::Other_buildings::Occupied_spaces`

### Credits and Post-Processing

The BREEAM daylight recipe automates the entire credit calculation during the post-processing phase. By cross-referencing the specific room programs you have assigned with the standard target thresholds outlined in the table below, the recipe evaluates your annual simulation data. 

It checks whether the required percentage of your floor area simultaneously meets both the **average daylight illuminance** and **minimum point illuminance** for the exact number of hours specified. The final output then tells you precisely how many credits your design has achieved.

<table>
  <thead>
    <tr>
      <th align="left">Area type</th>
      <th align="left">Credits</th>
      <th align="left">Minimum area to comply</th>
      <th align="left">Average daylight illuminance (averaged over entire space)</th>
      <th align="left">Minimum daylight illuminance at worst lit point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Education buildings</th>
    </tr>
    <tr>
      <td>Preschools, schools, further education - occupied spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td rowspan="3" align="left">At least 300 lux for 2000 hours per year or more</td>
      <td rowspan="3" align="left">At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <td>Higher education - occupied spaces</td>
      <td align="center">1</td>
      <td align="center">60%</td>
    </tr>
    <tr>
      <td>OR Higher education - occupied spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Healthcare buildings</th>
    </tr>
    <tr>
      <td>Staff and public areas</td>
      <td align="center">1</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <td>Occupied patients areas (dayrooms, wards) and consulting rooms</td>
      <td align="center">1</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <td>Staff and public areas</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2650 hours per year or more</td>
      <td>At least 90 lux for 2650 hours per year or more</td>
    </tr>
    <tr>
      <td>Occupied patients areas (dayrooms, wards) and consulting rooms</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2650 hours per year or more</td>
      <td>At least 90 lux for 2650 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Multi-residential buildings</th>
    </tr>
    <tr>
      <td>Kitchen</td>
      <td align="center">2</td>
      <td align="center">100%</td>
      <td>At least 100 lux for 3450 hours per year or more</td>
      <td>At least 30 lux for 3450 hours per year or more</td>
    </tr>
    <tr>
      <td>Living rooms, dining rooms, studies (including home offices)</td>
      <td align="center">2</td>
      <td align="center">100%</td>
      <td>At least 100 lux for 3450 hours. per year or more</td>
      <td>At least 30 lux for 3450 hours per year or more</td>
    </tr>
    <tr>
      <td>Non-residential or communal occupied spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 200 lux for 2650 hours per year or more</td>
      <td>At least 60 lux for 2650 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Retail buildings</th>
    </tr>
    <tr>
      <td>Sales areas</td>
      <td align="center">1</td>
      <td align="center">35%</td>
      <td colspan="2">At least 200 lux point daylight illuminances for 2650 hours per year or more</td>
    </tr>
    <tr>
      <td>Other occupied areas</td>
      <td align="center">1</td>
      <td align="center">80%</td>
      <td>At least 200 lux for 2650 hours per year or more</td>
      <td>At least 60 lux for 2650 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Prison buildings</th>
    </tr>
    <tr>
      <td>Cells and custody cells</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 100 lux for 3150 hours per year or more</td>
      <td align="center">N/A</td>
    </tr>
    <tr>
      <td>Internal association or atrium</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2650 hours per year or more</td>
      <td>At least 210 lux for 2650 hours per year</td>
    </tr>
    <tr>
      <td>Patient care spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2650 hours per year or more</td>
      <td>At least 210 lux for 2650 hours per year or more</td>
    </tr>
    <tr>
      <td>Teaching, lecture and seminar spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Office buildings</th>
    </tr>
    <tr>
      <td>All occupied spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours. per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Crèche buildings</th>
    </tr>
    <tr>
      <td>All occupied spaces</td>
      <td align="center">2</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
    <tr>
      <th colspan="5" align="left" style="background-color: #111111; color: #ffffff; padding: 10px;">Courts, Industrial and all Other building types</th>
    </tr>
    <tr>
      <td>All occupied spaces</td>
      <td align="center">1</td>
      <td align="center">80%</td>
      <td>At least 300 lux for 2000 hours per year or more</td>
      <td>At least 90 lux for 2000 hours per year or more</td>
    </tr>
  </tbody>
</table>
