#include <string>


class RitaUi {
  public:
    RitaUI();

    void get_screen_state(std::string &lin_1, std::string &lin_2);

  private:
    // Variables that hold the active lines (currently displayed on the lcd)
    std::string active_lin_1;
    std::string active_lin_2;


}