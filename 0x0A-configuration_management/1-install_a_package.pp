# This manifest file install Flask version 2.1.0 package from pip3
package{'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
