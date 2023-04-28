add_library(memora_server_lib STATIC memora_server.c)
target_include_directories(memora_server_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(memora_server_lib ${CHECK_LIBRARIES})

add_executable(memora_server main.c)
target_link_libraries(memora_server memora_server_lib memora)
