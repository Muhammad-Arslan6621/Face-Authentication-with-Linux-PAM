#include <security/pam_modules.h>
#include <security/pam_ext.h>
#include <syslog.h>
#include <stdlib.h>
#include <stdio.h>
#include <pwd.h>
#include <unistd.h>


int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    const char *username;
    if (pam_get_user(pamh, &username, "Username: ") != PAM_SUCCESS) {
        pam_syslog(pamh, LOG_ERR, "Failed to get username");
        return PAM_AUTH_ERR;  // Abort authentication if we can't retrieve username
    }
    
    pam_syslog(pamh, LOG_DEBUG, "Authenticating user: %s", username);
    // setup_environment(pamh, username);  // Set up the environment

    char command[512];
    snprintf(command, sizeof(command),
    "sudo -Hu %s DISPLAY=:0 XAUTHORITY=/run/user/1000/gdm/Xauthority "
    "python3 /home/aether_quasar/Videos/os_project/authenticate_face_old.py", username);

    
    pam_syslog(pamh, LOG_DEBUG, "Executing command: %s", command);
    
    int result = system(command);
    if (result == -1) {
        pam_syslog(pamh, LOG_ERR, "Failed to execute command");
        return PAM_AUTH_ERR;
    }

    // Extract the exit status of the command
    int exit_status = WEXITSTATUS(result);
    pam_syslog(pamh, LOG_DEBUG, "Command exit status: %d", exit_status);
    
    if (WIFEXITED(result)) {
        if (exit_status == 0) {
            pam_syslog(pamh, LOG_NOTICE, "Face authentication successful");
            return PAM_SUCCESS;  // Authentication success
        } 
        else if (exit_status == 2) {
            pam_syslog(pamh, LOG_ERR, "Face not recognized");
            pam_error(pamh, "Face not recognized. Please try again.");
            return PAM_AUTH_ERR;  // Face not recognized
        } 
        else {
            pam_syslog(pamh, LOG_ERR, "Face authentication failed with exit code: %d", exit_status);
        }
    } 
    else {
        pam_syslog(pamh, LOG_ERR, "Command failed to execute properly");
    }
    
    return PAM_AUTH_ERR;  // Authentication failed
}
