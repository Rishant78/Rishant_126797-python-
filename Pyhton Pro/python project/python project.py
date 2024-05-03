import random
import math

def calculate_beam_divergence():
    # Function to calculate beam divergence
    print("Performing numerical calculation (Beam Divergence)...\n")

    # Prompt the user for input
    initial_diameter = float(input("Enter the initial diameter of the beam (mm): "))
    divergence_angle = float(input("Enter the divergence angle of the beam (radians): "))
    distance = float(input("Enter the distance the beam propagates (meters): "))

    # Beam divergence calculation
    final_diameter = initial_diameter + 2 * divergence_angle * distance

    # Print the result
    print(f"\nThe final diameter of the beam after propagating a distance of {distance} meters is {final_diameter} mm.")

def calculate_beam_propagation():
    # Function to calculate beam propagation through a medium
    print("Performing numerical calculation (Beam Propagation through a Medium)...\n")

    # Prompt the user for input
    wavelength = float(input("Enter the wavelength of the laser beam (nm): "))
    refractive_index = float(input("Enter the refractive index of the medium: "))
    initial_diameter = float(input("Enter the initial diameter of the beam (mm): "))
    distance = float(input("Enter the distance the beam propagates (meters): "))

    # Beam propagation calculation
    final_diameter = initial_diameter * math.sqrt(1 + (wavelength * wavelength / (math.pi * initial_diameter * initial_diameter)) * (distance * distance) * ((refractive_index * refractive_index) - 1))

    # Print the result
    print(f"\nThe diameter of the beam after propagating {distance} meters through the medium is {final_diameter} mm.")

    # Function to calculate laser gain
def calculate_laser_gain(pump_power, quantum_efficiency):
    return pump_power * quantum_efficiency

# Function to calculate laser threshold
def calculate_laser_threshold(cavity_losses, gain_coefficient):
    return cavity_losses / gain_coefficient

# Function to calculate laser output power
def calculate_laser_output_power(pump_power, laser_efficiency, cavity_losses):
    return pump_power * laser_efficiency * (1 - cavity_losses)

# Function to display the results
def display_results(result, label):
    print(f"\nThe {label} is: {result} watts.")

def display_theory_laser():
    # Placeholder function for displaying laser theory
    print("\n**Theory of Laser Beam Propagation**\n")
    print("Laser beams propagate through mediums by interacting with atoms or molecules present in the material.\nThis interaction leads to several phenomena, including absorption,\nstimulated emission, and scattering, which collectively determine the behavior of the laser beam as it traverses the medium.")
    print("\n**Basic Principle of Laser Operation**\n")
    print("At the heart of a laser's functionality lies the principle of stimulated emission.\nThis process leads to the amplification of light, forming the basis of laser operation.")
    print("\n**Laser Gain Medium**\n")
    print("The medium through which the laser beam propagates, known as the laser gain medium, plays a crucial role in determining its characteristics.")
    print("\n**Interaction with Matter**\n")
    print("Laser light interacts with matter primarily through absorption, reflection, scattering, and refraction processes.")
    print("\n**Effects of Medium Properties**\n")
    print("The properties of the medium, including its refractive index, absorption coefficient, scattering coefficient,\ndensity, and temperature, profoundly influence laser beam propagation.")
    print("\n**Laser Cavity and Emission**\n")
    print("Laser operation requires a cavity containing the gain medium and mirrors.\nStimulated emission within the cavity leads to the amplification of light and eventual emission through a partially transparent mirror.")
    print("\n**Types of Lasers**\n")
    print("Lasers come in various types based on their gain medium and operation principles, including gas lasers,\nsolid-state lasers, semiconductor lasers, dye lasers, and fiber lasers.")
    print("\n**Characteristics of Laser Beams**\n")
    print("Laser beams possess unique characteristics such as coherence,\nmonochromaticity, and directionality, making them suitable for diverse applications.")
    print("\n**Applications of Lasers**\n")
    print("Lasers find applications in telecommunications, medicine, manufacturing, spectroscopy, navigation, research, and more.")
    print("\n**Future Trends**\n")
    print("The future of laser technology holds promise with ongoing advancements focused on compactness, efficiency, and novel applications.")
    # Laser theory content...

def display_theory_fiber():
    # Placeholder function for displaying fiber theory
    print("\n**Theory of Optical Fiber**\n")
    print("Optical fibers are thin, flexible, and transparent fibers that transmit light signals over long distances through total internal reflection.")
    print("\n**Basic Principle of Optical Fiber**\n")
    print("The basic principle of optical fibers relies on total internal reflection, which occurs when light traveling within the fiber core strikes the boundary with the cladding at an angle greater than the critical angle.")
    print("\n**Components of Optical Fiber**\n")
    print("An optical fiber consists of a core, which carries the light signal, surrounded by a cladding layer that ensures total internal reflection, and a protective outer layer.")
    print("\n**Types of Optical Fiber**\n")
    print("Optical fibers come in various types, including single-mode fiber and multi-mode fiber, each suited for different applications based on their core size and the way light propagates through them.")
    print("\n**Optical Fiber Characteristics**\n")
    print("Optical fibers offer advantages such as low attenuation, high bandwidth, immunity to electromagnetic interference, and flexibility, making them ideal for telecommunications, data transmission, and networking applications.")
    print("\n**Applications of Optical Fiber**\n")
    print("Optical fibers find applications in telecommunications, internet connectivity, cable television, medical imaging, sensing, and more.")
    print("\n**Future Trends**\n")
    print("The future of optical fiber technology involves advancements in higher data rates, increased transmission distances, and improved efficiency for various applications.")
    # Fiber theory content...

def run_quiz(questions):
    # Initialize score
    score = 0

    # Run the quiz
    for i, question in enumerate(questions[:25]): # Limiting to 25 questions
        print(f"\nQuestion {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    # Display final score
    print(f"\nYour score: {score}/{min(len(questions), 25)}")

def calculate_laser_gain(pump_power, quantum_efficiency):
    # Function to calculate laser gain
    return pump_power * quantum_efficiency

def calculate_laser_threshold(cavity_losses, gain_coefficient):
    # Function to calculate laser threshold
    return cavity_losses / gain_coefficient

def calculate_laser_output_power(pump_power, laser_efficiency, cavity_losses):
    # Function to calculate laser output power
    return pump_power * laser_efficiency * (1 - cavity_losses)

def calculate_optical_fiber_attenuation(initial_power, final_power, distance):
    # Function to calculate optical fiber attenuation
    return 10 * math.log10(initial_power / final_power) / distance

def calculate_optical_fiber_numerical_aperture(n_core, n_cladding):
    # Function to calculate optical fiber numerical aperture
    return math.sqrt(n_core ** 2 - n_cladding ** 2)

def calculate_optical_fiber_acceptance_angle(numerical_aperture):
    # Function to calculate optical fiber acceptance angle
    return math.degrees(math.asin(numerical_aperture))

def calculate_optical_fiber_modal_dispersion(core_diameter, wavelength, refractive_index_difference):
    # Function to calculate optical fiber modal dispersion
    return (core_diameter ** 2) * (wavelength ** 2) * refractive_index_difference / (8 * 10 ** 12)

def run_numerical_calculations_laser():
    while True:
        print("\nSelect an option for numerical calculation:")
        print("1. Calculate Beam Divergence")
        print("2. Calculate Beam Propagation through a Medium")
        print("3. Calculate Laser Gain")
        print("4. Calculate Laser Threshold")
        print("5. Calculate Laser Output Power")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            calculate_beam_divergence()

        elif choice == '2':
            calculate_beam_propagation()

        elif choice == '3':
            # Prompt user for input
            print("Example values:")
            print("Pump power (in watts): 10")
            print("Quantum efficiency of the gain medium: 0.8")
            pump_power = float(input("Enter the pump power (in watts): "))
            quantum_efficiency = float(input("Enter the quantum efficiency of the gain medium: "))

            # Calculate laser gain
            laser_gain = calculate_laser_gain(pump_power, quantum_efficiency)
            display_results(laser_gain, "laser gain")

        elif choice == '4':
            # Prompt user for input
            print("Example values:")
            print("Cavity losses: 0.1")
            print("Gain coefficient of the gain medium: 0.5")
            cavity_losses = float(input("Enter the cavity losses: "))
            gain_coefficient = float(input("Enter the gain coefficient of the gain medium: "))

            # Calculate laser threshold
            laser_threshold = calculate_laser_threshold(cavity_losses, gain_coefficient)
            display_results(laser_threshold, "laser threshold pump power")

        elif choice == '5':
            # Prompt user for input
            print("Example values:")
            print("Pump power (in watts): 20")
            print("Efficiency of the laser: 0.9")
            print("Cavity losses: 0.2")
            pump_power = float(input("Enter the pump power (in watts): "))
            laser_efficiency = float(input("Enter the efficiency of the laser: "))
            cavity_losses = float(input("Enter the cavity losses: "))

            # Calculate laser output power
            laser_output_power = calculate_laser_output_power(pump_power, laser_efficiency, cavity_losses)
            display_results(laser_output_power, "laser output power")

        elif choice == '6':
            # Exit
            print("Exiting the numerical calculations.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
def run_numerical_calculations_fiber():
    while True:
        print("\nSelect an option for numerical calculation:")
        print("1. Calculate Optical Fiber Attenuation")
        print("2. Calculate Optical Fiber Numerical Aperture")
        print("3. Go back to previous menu")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Prompt user for input
            print("Example values:")
            print("Initial power of the signal (in mW): 10")
            print("Final power of the signal (in mW): 5")
            print("Distance the signal travels (in km): 10")
            initial_power = float(input("Enter the initial power of the signal (in mW): "))
            final_power = float(input("Enter the final power of the signal (in mW): "))
            distance = float(input("Enter the distance the signal travels (in km): "))

            # Calculate optical fiber attenuation
            attenuation = calculate_optical_fiber_attenuation(initial_power, final_power, distance)
            print(f"\nThe attenuation of the optical fiber is {attenuation} dB/km.")

        elif choice == '2':
            # Prompt user for input
            print("Example values:")
            print("Refractive index of the core: 1.5")
            print("Refractive index of the cladding: 1.45")
            n_core = float(input("Enter the refractive index of the core: "))
            n_cladding = float(input("Enter the refractive index of the cladding: "))

            # Calculate optical fiber numerical aperture
            numerical_aperture = calculate_optical_fiber_numerical_aperture(n_core, n_cladding)
            print(f"\nThe numerical aperture of the optical fiber is {numerical_aperture}.")

        elif choice == '3':
            # Go back to previous menu
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
def main():
    # Define quiz questions and answers for LASER
    laser_quiz_questions = [
        {"question": "What does LASER stand for?", "options": ["Light Amplification by Stimulated Emission of Radiation", "Light Absorption by Stimulated Emission of Radiation", "Laser Amplification by Stimulated Emission of Reflection", "Light Amplification by Stimulation of Reflection"], "answer": 0},
        {"question": "Who invented the first laser?", "options": ["Albert Einstein", "Isaac Newton", "Charles Darwin", "Theodore Maiman"], "answer": 3},
        {"question": "What is the principle behind laser beam propagation?", "options": ["Diffraction", "Refraction", "Interference", "Stimulated emission"], "answer": 3},
        {"question": "What is the main advantage of a laser over other light sources?", "options": ["Coherence", "Brightness", "Monochromaticity", "All of the above"], "answer": 3},
        {"question": "Which material is commonly used as the gain medium in gas lasers?", "options": ["Ruby", "Neon", "YAG", "Helium-Neon"], "answer": 1},
        {"question": "What is the unit of wavelength of light?", "options": ["Meter", "Nanometer", "Angstrom", "Micrometer"], "answer": 1},
        {"question": "Which of the following is NOT a type of laser?", "options": ["Diode laser", "Fiber laser", "Electric laser", "Dye laser"], "answer": 2},
        {"question": "What is the minimum number of energy levels required for laser operation?", "options": ["1", "2", "3", "4"], "answer": 1},
        {"question": "Which of the following is an example of a continuous-wave laser?", "options": ["Ruby laser", "Pulsed dye laser", "Excimer laser", "CO2 laser"], "answer": 0},
        {"question": "Which laser type is commonly used in laser printers?", "options": ["Ruby laser", "CO2 laser", "Semiconductor laser", "Dye laser"], "answer": 2},
        {"question": "What is the primary mechanism by which laser light interacts with matter?", "options": ["Absorption", "Reflection", "Scattering", "Refraction"], "answer": 0},
        {"question": "What type of laser is commonly used in laser eye surgery?", "options": ["Excimer laser", "Ruby laser", "Gas laser", "Dye laser"], "answer": 0},
        {"question": "Which laser type typically emits ultraviolet light?", "options": ["Ruby laser", "YAG laser", "Excimer laser", "Fiber laser"], "answer": 2},
        {"question": "What is the name of the process by which atoms in an excited state emit photons?", "options": ["Absorption", "Stimulated emission", "Reflection", "Refraction"], "answer": 1},
        {"question": "Which type of laser uses a crystal doped with rare-earth ions as the gain medium?", "options": ["Fiber laser", "Solid-state laser", "Gas laser", "Dye laser"], "answer": 1},
        {"question": "Which laser type produces the shortest pulses?", "options": ["Excimer laser", "Dye laser", "Fiber laser", "Ultrafast laser"], "answer": 3},
        {"question": "Which laser type is commonly used in barcode scanners?", "options": ["CO2 laser", "Diode laser", "Helium-neon laser", "Semiconductor laser"], "answer": 3},
        {"question": "What is the name of the process by which a laser beam spreads out as it propagates?", "options": ["Reflection", "Refraction", "Diffraction", "Scattering"], "answer": 2},
        {"question": "Which laser type typically emits infrared light?", "options": ["Ruby laser", "YAG laser", "Excimer laser", "Dye laser"], "answer": 1},
        {"question": "What is the name of the device used to generate laser light?", "options": ["Laser diode", "Laser gun", "Laser printer", "Laser cavity"], "answer": 3},
        {"question": "What type of laser is commonly used in telecommunications?", "options": ["CO2 laser", "Fiber laser", "YAG laser", "Dye laser"], "answer": 1},
        {"question": "Which laser type is commonly used in cosmetic procedures such as hair removal?", "options": ["CO2 laser", "Diode laser", "Excimer laser", "Ruby laser"], "answer": 1},
        {"question": "Which laser type is commonly used in laser cutting and welding?", "options": ["CO2 laser", "Diode laser", "Fiber laser", "Ruby laser"], "answer": 2},
        {"question": "What is the name of the process by which a laser beam changes direction as it enters a different medium?", "options": ["Reflection", "Refraction", "Diffraction", "Scattering"], "answer": 1},
        {"question": "What is the name of the device used to select a specific wavelength of laser light?", "options": ["Laser diode", "Laser gun", "Laser printer", "Tunable laser"], "answer": 3},
        
        # Additional questions
        {"question": "Which laser type is commonly used in lidar systems?", "options": ["CO2 laser", "Fiber laser", "Semiconductor laser", "Dye laser"], "answer": 1},
        {"question": "What is the principle behind a Q-switched laser?", "options": ["Continuous emission", "Pulsed emission", "Single-mode emission", "Mode-locked emission"], "answer": 3},
        {"question": "Which laser type is commonly used in military applications such as rangefinding and target designation?", "options": ["CO2 laser", "Excimer laser", "Diode-pumped solid-state laser", "Helium-neon laser"], "answer": 2},
        {"question": "What is the phenomenon that leads to the formation of a laser beam's speckle pattern?", "options": ["Interference", "Diffraction", "Scattering", "Refraction"], "answer": 0},
        {"question": "In what year was the first working laser demonstrated?", "options": ["1947", "1958", "1960", "1972"], "answer": 2},
        {"question": "Which laser type is commonly used in high-power industrial cutting applications?", "options": ["CO2 laser", "Fiber laser", "Dye laser", "Excimer laser"], "answer": 1},
        {"question": "What is the name of the process used to cool laser gain media to maintain their optimal operating temperature?", "options": ["Laser cooling", "Thermal stabilization", "Cryogenic cooling", "Active cooling"], "answer": 0},
        {"question": "Which laser type is commonly used in environmental monitoring for detecting atmospheric pollutants?", "options": ["CO2 laser", "Tunable diode laser", "Excimer laser", "Fiber laser"], "answer": 1},
        {"question": "What is the name of the phenomenon where a laser beam spreads due to differences in refractive index across its cross-section?", "options": ["Beam collimation", "Beam divergence", "Beam diffusion", "Beam dispersion"], "answer": 1},
        {"question": "Which laser type is commonly used in ophthalmology for procedures like retinal photocoagulation?", "options": ["CO2 laser", "Excimer laser", "Nd:YAG laser", "Dye laser"], "answer": 2},
        {"question": "What is the primary mechanism behind laser-induced breakdown spectroscopy (LIBS)?", "options": ["Absorption", "Emission", "Ionization", "Scattering"], "answer": 2},
        {"question": "Which laser type is commonly used in quantum computing experiments due to its ability to trap and cool atoms?", "options": ["CO2 laser", "Fiber laser", "Diode laser", "Optical lattice laser"], "answer": 3},
        {"question": "What is the name of the process where a laser beam is focused to a small spot with high intensity?", "options": ["Beam compression", "Beam concentration", "Beam focusing", "Beam condensation"], "answer": 2},
    ]

    # Define quiz questions and answers for Optical Fiber
    fiber_quiz_questions = [
    {"question": "What is the primary function of optical fibers?", "options": ["Data transmission", "Electrical power transmission", "Heat conduction", "Water transport"], "answer": 0},
    {"question": "What material is commonly used for the core of an optical fiber?", "options": ["Silica (Glass)", "Copper", "Aluminum", "Plastic"], "answer": 0},
    {"question": "What is the typical refractive index of the core in an optical fiber?", "options": ["Higher than that of the cladding", "Lower than that of the cladding", "Equal to that of the cladding", "There is no core in an optical fiber"], "answer": 0},
    {"question": "What is the purpose of the cladding in an optical fiber?", "options": ["To protect the core from damage", "To enhance light transmission", "To reduce signal loss", "All of the above"], "answer": 3},
    {"question": "What is the function of the optical fiber buffer?", "options": ["To provide mechanical strength", "To protect the cladding", "To enhance signal quality", "None of the above"], "answer": 0},
    {"question": "Which type of optical fiber has a solid glass core surrounded by a glass cladding?", "options": ["Single-mode fiber", "Multimode fiber", "Step-index fiber", "Graded-index fiber"], "answer": 0},
    {"question": "What is the typical diameter of the core in a single-mode optical fiber?", "options": ["Around 9 micrometers", "Around 50 micrometers", "Around 125 micrometers", "Around 200 micrometers"], "answer": 0},
    {"question": "What is the advantage of single-mode fibers over multimode fibers?", "options": ["Higher bandwidth and longer transmission distances", "Lower cost", "Simpler installation", "Greater tolerance to bending"], "answer": 0},
    {"question": "What is the purpose of the cladding in an optical fiber?", "options": ["To guide light by total internal reflection", "To amplify the signal", "To reduce dispersion", "To increase attenuation"], "answer": 0},
    {"question": "What is the typical refractive index of the cladding in an optical fiber?", "options": ["Lower than that of the core", "Higher than that of the core", "Equal to that of the core", "Depends on the fiber type"], "answer": 0},
    {"question": "What is the purpose of the optical fiber coating?", "options": ["To protect the fiber from mechanical damage", "To improve light transmission", "To increase the refractive index", "To reduce attenuation"], "answer": 0},
    {"question": "What is the most common method of connecting optical fibers?", "options": ["Fusion splicing", "Mechanical splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the main cause of signal loss in optical fibers?", "options": ["Attenuation", "Dispersion", "Reflection", "Scattering"], "answer": 0},
    {"question": "Which type of dispersion is caused by differences in arrival times of different wavelengths of light?", "options": ["Chromatic dispersion", "Modal dispersion", "Polarization mode dispersion", "Waveguide dispersion"], "answer": 0},
    {"question": "What is the typical wavelength range used in optical fiber communication?", "options": ["Around 1310 nm and 1550 nm", "Around 850 nm and 1300 nm", "Around 650 nm and 850 nm", "Around 1550 nm and 1625 nm"], "answer": 0},
    {"question": "What is the primary factor limiting the transmission distance in optical fiber communication?", "options": ["Attenuation", "Dispersion", "Reflection", "Scattering"], "answer": 0},
    {"question": "What is the term for the phenomenon where light exits the fiber core due to imperfections in the cladding?", "options": ["Leakage", "Reflection", "Dispersion", "Scattering"], "answer": 0},
    {"question": "What is the name for the bending-induced attenuation in optical fibers?", "options": ["Macro bending loss", "Micro bending loss", "Fresnel loss", "Rayleigh scattering"], "answer": 0},
    {"question": "Which type of optical fiber has a core with varying refractive index?", "options": ["Graded-index fiber", "Step-index fiber", "Single-mode fiber", "Multimode fiber"], "answer": 0},
    {"question": "What is the main advantage of graded-index fibers over step-index fibers?", "options": ["Lower modal dispersion", "Higher bandwidth", "Lower attenuation", "Easier manufacturing"], "answer": 0},
    {"question": "What is the name for the phenomenon where light is scattered due to variations in the refractive index of the fiber?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of joining two optical fibers end-to-end?", "options": ["Splicing", "Cleaving", "Termination", "Fusion bonding"], "answer": 0},
    {"question": "What is the typical diameter of the cladding in an optical fiber?", "options": ["Around 125 micrometers", "Around 9 micrometers", "Around 50 micrometers", "Around 200 micrometers"], "answer": 0},
    {"question": "Which type of optical fiber allows only one mode of light to propagate?", "options": ["Single-mode fiber", "Multimode fiber", "Graded-index fiber", "Step-index fiber"], "answer": 0},
    {"question": "What is the name for the phenomenon where light is reflected back into the core due to imperfections in the cladding?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Mode hopping"], "answer": 0},
    {"question": "Which type of optical fiber has a core with a constant refractive index?", "options": ["Step-index fiber", "Graded-index fiber", "Single-mode fiber", "Multimode fiber"], "answer": 0},
    {"question": "What is the typical diameter of the coating in an optical fiber?", "options": ["Around 250 micrometers", "Around 9 micrometers", "Around 125 micrometers", "Around 50 micrometers"], "answer": 0},
    {"question": "What is the name for the process of cutting an optical fiber to create a flat end face?", "options": ["Cleaving", "Splicing", "Termination", "Fusion bonding"], "answer": 0},
    {"question": "What is the name for the region of an optical fiber where the core and cladding are fused together?", "options": ["Fusion zone", "Splice point", "Core junction", "Cladding boundary"], "answer": 0},
    {"question": "Which type of optical fiber has a core with a step-like refractive index profile?", "options": ["Step-index fiber", "Graded-index fiber", "Single-mode fiber", "Multimode fiber"], "answer": 0},
    {"question": "What is the name for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "What is the term for the bending-induced attenuation in optical fibers that occurs on a larger scale?", "options": ["Macro bending loss", "Micro bending loss", "Fresnel loss", "Rayleigh scattering"], "answer": 0},
    {"question": "What is the term for the process of connecting optical fibers using an adhesive?", "options": ["Termination", "Splicing", "Cleaving", "Fusion bonding"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using heat?", "options": ["Fusion splicing", "Mechanical splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the typical refractive index of the coating in an optical fiber?", "options": ["Lower than that of the cladding", "Higher than that of the cladding", "Equal to that of the cladding", "Depends on the fiber type"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of removing the protective coating from an optical fiber?", "options": ["Stripping", "Termination", "Splicing", "Fusion bonding"], "answer": 0},
    {"question": "What is the term for the process of connecting optical fibers without the use of heat?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for long-haul transmission?", "options": ["Around 1550 nm", "Around 850 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0},
    {"question": "Which type of optical fiber has a core with a gradually changing refractive index?", "options": ["Graded-index fiber", "Step-index fiber", "Single-mode fiber", "Multimode fiber"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is scattered due to imperfections in the fiber material?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using mechanical fixtures?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power due to bending of the optical fiber?", "options": ["Bend loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "Which type of dispersion is caused by variations in the refractive index of the fiber material?", "options": ["Waveguide dispersion", "Modal dispersion", "Chromatic dispersion", "Polarization mode dispersion"], "answer": 0},
    {"question": "What is the name for the process of bending an optical fiber to the point where it breaks?", "options": ["Cleaving", "Fusion splicing", "Fracturing", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using an adhesive?", "options": ["Adhesive bonding", "Fusion splicing", "Cleaving", "Mechanical splicing"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for short-distance transmission?", "options": ["Around 850 nm", "Around 1550 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is scattered due to imperfections in the fiber material?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using mechanical fixtures?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power due to bending of the optical fiber?", "options": ["Bend loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "Which type of dispersion is caused by variations in the refractive index of the fiber material?", "options": ["Waveguide dispersion", "Modal dispersion", "Chromatic dispersion", "Polarization mode dispersion"], "answer": 0},
    {"question": "What is the name for the process of bending an optical fiber to the point where it breaks?", "options": ["Cleaving", "Fusion splicing", "Fracturing", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using an adhesive?", "options": ["Adhesive bonding", "Fusion splicing", "Cleaving", "Mechanical splicing"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for short-distance transmission?", "options": ["Around 850 nm", "Around 1550 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is scattered due to imperfections in the fiber material?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using mechanical fixtures?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power due to bending of the optical fiber?", "options": ["Bend loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "Which type of dispersion is caused by variations in the refractive index of the fiber material?", "options": ["Waveguide dispersion", "Modal dispersion", "Chromatic dispersion", "Polarization mode dispersion"], "answer": 0},
    {"question": "What is the name for the process of bending an optical fiber to the point where it breaks?", "options": ["Cleaving", "Fusion splicing", "Fracturing", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using an adhesive?", "options": ["Adhesive bonding", "Fusion splicing", "Cleaving", "Mechanical splicing"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for short-distance transmission?", "options": ["Around 850 nm", "Around 1550 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is scattered due to imperfections in the fiber material?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using mechanical fixtures?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power due to bending of the optical fiber?", "options": ["Bend loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "Which type of dispersion is caused by variations in the refractive index of the fiber material?", "options": ["Waveguide dispersion", "Modal dispersion", "Chromatic dispersion", "Polarization mode dispersion"], "answer": 0},
    {"question": "What is the name for the process of bending an optical fiber to the point where it breaks?", "options": ["Cleaving", "Fusion splicing", "Fracturing", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using an adhesive?", "options": ["Adhesive bonding", "Fusion splicing", "Cleaving", "Mechanical splicing"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for short-distance transmission?", "options": ["Around 850 nm", "Around 1550 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is scattered due to imperfections in the fiber material?", "options": ["Rayleigh scattering", "Fresnel loss", "Total internal reflection", "Chromatic dispersion"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using mechanical fixtures?", "options": ["Mechanical splicing", "Fusion splicing", "Cleaving", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power due to bending of the optical fiber?", "options": ["Bend loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the term for the phenomenon where light is reflected back into the core due to changes in refractive index along the fiber?", "options": ["Fresnel reflection", "Rayleigh scattering", "Chromatic dispersion", "Total internal reflection"], "answer": 0},
    {"question": "Which type of dispersion is caused by variations in the refractive index of the fiber material?", "options": ["Waveguide dispersion", "Modal dispersion", "Chromatic dispersion", "Polarization mode dispersion"], "answer": 0},
    {"question": "What is the name for the process of bending an optical fiber to the point where it breaks?", "options": ["Cleaving", "Fusion splicing", "Fracturing", "Adhesive bonding"], "answer": 0},
    {"question": "What is the term for the loss of signal power at a joint between two optical fibers?", "options": ["Splice loss", "Attenuation", "Dispersion", "Reflection"], "answer": 0},
    {"question": "What is the name for the process of aligning and joining optical fibers using an adhesive?", "options": ["Adhesive bonding", "Fusion splicing", "Cleaving", "Mechanical splicing"], "answer": 0},
    {"question": "What is the typical wavelength used in optical fiber communication for short-distance transmission?", "options": ["Around 850 nm", "Around 1550 nm", "Around 1310 nm", "Around 650 nm"], "answer": 0}
]


    while True:
        print("\nSelect an option:")
        print("1. LASER")
        print("2. Optical Fibre")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Laser operations
            while True:
                print("\nLASER Operations:")
                print("1. Display theory")
                print("2. Perform numerical calculations")
                print("3. Run quiz")
                print("4. Go back to previous menu")
                sub_choice = input("Enter your choice (1-4): ")

                if sub_choice == '1':
                    # Display laser theory
                    display_theory_laser()

                elif sub_choice == '2':
                    # Numerical calculations for laser
                    run_numerical_calculations_laser()

                elif sub_choice == '3':
                    # Run laser quiz
                    run_quiz(laser_quiz_questions)

                elif sub_choice == '4':
                    # Go back to previous menu
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == '2':
            # Optical fiber operations
            while True:
                print("\nOptical Fibre Operations:")
                print("1. Display theory")
                print("2. Perform numerical calculations")
                print("3. Run quiz")
                print("4. Go back to previous menu")
                sub_choice = input("Enter your choice (1-4): ")

                if sub_choice == '1':
                    # Display fiber theory
                    display_theory_fiber()

                elif sub_choice == '2':
                    # Numerical calculations for fiber
                    run_numerical_calculations_fiber()

                elif sub_choice == '3':
                    # Run fiber quiz
                    run_quiz(fiber_quiz_questions)

                elif sub_choice == '4':
                    # Go back to previous menu
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == '3':
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
