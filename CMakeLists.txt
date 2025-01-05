cmake_minimum_required(VERSION 3.13)

# Set the name and version of the project
set(PROJECT_NAME RitaOS)
project(${PROJECT_NAME} C CXX ASM)


# Set the C standard to C11 and the C++ standard to C++20
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 20)

# Set Pico SDK Path
set(PICO_SDK_PATH ${CMAKE_SOURCE_DIR}/pico-sdk)

include(lib/FreeRTOS-Kernel/portable/ThirdParty/GCC/RP2040/FreeRTOS_Kernel_import.cmake) ## Import FreeRTOS Kernel
include(pico_sdk_import.cmake)

# Initialize the Pico SDK
include(${PICO_SDK_PATH}/pico_sdk_init.cmake)
include(${PICO_SDK_PATH}/pico_sdk_version.cmake)
configure_file(
    ${PICO_SDK_PATH}/src/common/pico_base_headers/include/pico/version.h.in
    ${CMAKE_BINARY_DIR}/generated/pico/version.h
)

pico_sdk_init()




# Set target name
set(TARGET_NAME ${PROJECT_NAME})


# ARM GCC Compiler stuff from GPT
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)

# Add the source files to the target
add_executable(${TARGET_NAME}
	src/main.c
)

# Enable USB and/or UART output
# pico_enable_stdio_uart(${TARGET_NAME} 1)
# pico_enable_stdio_usb(${TARGET_NAME} 1)


target_compile_definitions(${TARGET_NAME} PRIVATE
)



# Line to help FreeRTOS Kernel to find the configuration file in the current directory
target_include_directories(${TARGET_NAME} PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}
    # ${CMAKE_BINARY_DIR}/generated/pico
    # ${PICO_SDK_PATH}/bazel/include  # Add the Bazel include directory here
    )

# target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_BINARY_DIR}/generated)

## usb and uart
pico_enable_stdio_uart(${TARGET_NAME} 1)
pico_enable_stdio_usb(${TARGET_NAME} 1)


target_link_libraries(${TARGET_NAME} PRIVATE
    pico_stdlib
    hardware_gpio
    pico_multicore

    FreeRTOS-Kernel
    FreeRTOS-Kernel-Heap4
)

pico_add_extra_outputs(${TARGET_NAME})